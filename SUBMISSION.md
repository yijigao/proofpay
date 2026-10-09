# Devpost submission draft (English)

## Title
ProofPay — escrow for AI work: frozen first, paid only when the output checks out

## Tagline
Your money is authorized, not spent. Nine objective checks decide: pass → capture, fail → void.

## Problem
Buying AI-generated content today is pay-first-and-pray: if the output has a wrong price,
a fake source link, or stale data, the buyer has already paid. Refunds and disputes are
slow, manual, and rare.

## Solution
ProofPay wraps a PayPal AUTHORIZE/CAPTURE flow around AI generation:
1. Buyer places a task (deliverable spec + data snapshot). PayPal only freezes the funds.
2. An AI generates the deliverable strictly from the frozen snapshot (here: a deal brief
   built from a PriceScout price feed).
3. Nine objective, re-runnable checks verify the output — count, length, SKU↔source
   binding, price, currency, freshness window (both bounds), deadline sanity, amount,
   dedup + version.
4. 9/9 pass → capture. Any failure → void; the buyer pays $0.00 and gets the failed-item list.

## Why it matters
It turns "trust the AI" into "verify the AI" — a reusable settlement layer for
agentic commerce: content shops, research briefs, data summaries, any AI deliverable
that can be checked objectively before money moves.

## Tech
- PayPal sandbox Orders v2 (AUTHORIZE intent) + Payments v2 (capture/void), verified
  end-to-end in sandbox on 2026-10-09 (capture COMPLETED; void VOIDED).
- Python stdlib demo app (order / verification / receipt pages), deterministic generator,
  offline checker CLI. Snapshot format reuses the PriceScout feed.

## Honest scope
Amount-to-live-order binding, cross-task id uniqueness, and generator-version
authenticity are noted as v1 gaps in the README — we show exactly what is verified
and what is not.

## AI tools used
Muse / GPT-class coding agents for implementation assistance (disclosed per rules).
