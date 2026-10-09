# YouTube upload pack (ready for Joey, public visibility)

## Title
ProofPay — Pay for AI Work Only When It Checks Out (PayPal AI Hackathon)

## Description
ProofPay is an escrow pattern for agentic commerce: when you buy AI-generated
content, your money is authorized (frozen), not paid. The AI generates the
deliverable from a frozen data snapshot, then nine objective, re-runnable
checks decide the outcome:

• 9/9 pass → the frozen authorization is captured
• Any failure → the authorization is voided and you pay $0.00

What you see in this video: a local simulated demo. It shows a capture
decision (9/9 green lights) and a complete fault-injected void path (one
wrong price turns the price check red, the authorization is voided, the
buyer pays $0.00). The capture receipt itself is not shown in this cut.
Footage is a local simulation; no money moved and no live PayPal calls
happen on screen.

Separately, the README records PayPal sandbox API tests from 2026-10-09
(test money only): authorize 201 → capture 201 COMPLETED, and authorize
201 → void 204 → VOIDED. Transaction IDs are not supplied; the on-screen
task id is a local demo id, not a PayPal order id.

Known gaps, stated plainly: live-order amount binding is not yet verified;
cross-task uniqueness and generator-version authenticity rely on
self-reported values without a trusted execution log. This local demo
mirrors separate sandbox API tests; no money moves.

Note on the burned-in captions: two captions in the film speak of the
capture in the past tense ("Paid $10.00 — capture COMPLETED"). Read them
as the decision shown on screen plus the separate sandbox result above —
the capture receipt is not part of this cut.

Open source (MIT). Run it yourself with no credentials:
https://github.com/yijigao/proofpay

Built for the PayPal AI Hackathon — Best Use of Agentic Commerce.
AI tools used: Claude/GPT-class coding agents (implementation assistance).

## Tags
PayPal, AI Hackathon, agentic commerce, escrow, AI agents, fintech, Devpost

## Settings checklist
- Visibility: Public
- Audience: Not made for kids
- Category: Science & Technology
- Language: English
