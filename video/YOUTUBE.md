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

In this 2-minute live demo you will see both endings: a deal brief that passes
all nine checks (count, length, SKU-source binding, price, currency, freshness
window, deadline, amount, dedup/version) and gets captured — and a
fault-injected run where one wrong price turns a check red, voids the
authorization, and costs the buyer nothing.

Payment flows verified end-to-end in the PayPal sandbox (test money only):
authorize 201 → capture 201 COMPLETED; authorize 201 → void 204 VOIDED.

Open source (MIT). Judges can run the demo with no credentials:
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
