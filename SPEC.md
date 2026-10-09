# ProofPay SPEC v0.1 (D1 定版)
概念：买家为 AI 内容服务下单，PayPal 先 AUTHORIZE 冻结；AI 基于数据快照生成内容，过九项客观核验才 capture，失败 void。

## 任务单 TaskOrder
fields: task_id, buyer_ref, service_type(deal_brief), snapshot_id, amount{value,currency}, deadline_utc, deliverable_spec{item_count, max_chars, required_fields}, status(PREPARED/AUTHORIZED/GENERATED/CHECKED/CAPTURED/VOIDED/FAILED), paypal{order_id, authorization_id, capture_id}, created_at
## 数据快照 Snapshot (PriceScout feed 复用)
fields: snapshot_id, taken_at_utc, source(pricescout-feed), items[{sku, title, price_old, price_new, currency, url, seen_at_utc}], feed_version
规则：生成只能引用快照内条目，价格/币种与快照一致，seen_at 至生成时差即数据时效校验项。
## 九项核验 (全客观、可重跑)
1 件数 = spec.item_count  2 长度 <= max_chars  3 来源 SKU↔URL 绑定（每条 url 必须等于快照中同一 SKU 的 url）  4 价格与快照一致  5 币种一致  6 数据时效 0 <= 生成时间-seen_at <= 24h（未来观测拒绝）  7 期限 生成时间 <= deadline 且 >= 快照 taken_at 且不晚于当前时刻（未来生成拒绝）  8 金额 任务金额 = 生成物声明金额（本地比对；与真实 PayPal 订单回执的绑定见仓 README 已知缺口）  9 去重 单次条目不重复 + 版本 生成器自报版本 = 任务单指定版本（跨任务 task_id 唯一性与版本真实性为已知缺口，见 README）
判定：9/9 PASS -> capture；任一 FAIL -> void 并回失败项清单。
2026-10-09 修订：按派工台离线反例审计（CE01/CE02/CE03）修复 3 处误放行：SKU-URL 错配、未来 seen_at、未来生成时间，复跑全过。
## 支付状态机
CREATED -> (buyer approve) -> AUTHORIZE -> auth_id -> [PASS capture | FAIL void]；每步落 paypal 返回状态与时间，幂等键 task_id。
