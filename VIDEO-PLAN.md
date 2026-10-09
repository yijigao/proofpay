# ProofPay 演示视频拟案（主聊 2026-10-09 审过，必改：总长 ≤2:45）
总长目标 2:40，全程真实界面（本地 app 三页面 + PayPal 沙盒返回），英文旁白/字幕，对齐五维评审：技术实现/设计/影响/创新/展示。

| 时间 | 画面 | 旁白要点 |
|---|---|---|
| 0:00–0:12 | 痛点字幕页 → 下单页（已削） | "Pay first, hope the AI output is right? ProofPay freezes your money instead — and only pays when the output checks out." |
| 0:12–0:40 | 下单页点击 Place order → 冻结状态（沙盒 authorize 201 证据字幕） | 买家下单，PayPal AUTHORIZE 只冻结 $10，未扣款 |
| 0:40–1:08 | 生成简讯出现 → 核验页九项逐项亮绿 | AI 基于 PriceScout 快照生成优惠简讯；九项客观核验逐项过：件数/长度/SKU↔链接绑定/价格/币种/时效双界/期限/金额/去重+版本 |
| 1:08–1:30 | 九绿 → Capture → 收据页 Paid $10.00（capture COMPLETED） | 9/9 才 capture，附 D1 沙盒实证单号字幕 |
| 1:30–2:05 | 勾选故障注入重跑 → 价格项红灯 → Void → 收据页 You pay $0.00 | 故意让 AI 用错价格：一项红灯即作废授权，买家零损失（void 204 VOIDED 实证单号） |
| 2:05–2:40 | 架构一页图 + GitHub 仓页（已削） | 复用说明：PriceScout feed、Scanner 规则核验框架、PayPal 沙盒；开源 MIT、评委可自跑；诚实口径：金额与真实订单回执绑定、跨任务唯一性为 v1 已知缺口，不吹已验证 |

拍摄注意：不出现任何凭据/邮箱密码；沙盒字样明示 test money；背景音乐用无版权素材；YouTube 公开上传由 Joey 账号执行（提交红线不变）。
