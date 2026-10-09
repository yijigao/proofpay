# ProofPay — pay for AI output only when it checks out

ProofPay is an agentic-commerce escrow pattern for buying AI-generated content:
the buyer's money is **authorized (frozen), not paid**. An AI generates the deliverable
from a frozen data snapshot; nine objective, re-runnable checks decide what happens next —
**9/9 pass → capture**, **any failure → void** (buyer pays $0.00).

Built for the PayPal AI Hackathon (target: Best Use of Agentic Commerce).

## The nine checks
1. Item count matches the task spec
2. Output length within spec
3. Every item's source URL is bound to the same SKU in the snapshot (no mismatched links)
4. Every price equals the snapshot price
5. Currency consistent
6. Data freshness: 0 ≤ generation − seen_at ≤ 24h (future observations rejected)
7. Deadline: generated on time, after the snapshot existed, and not in the future
8. Amount: generated amount equals the task amount (local comparison — see Known gaps)
9. No duplicate items; generator version matches the task spec (self-reported — see Known gaps)

## Run the demo (no credentials needed)
```bash
python3 src/app.py        # stdlib only, Python 3.10+
# open http://127.0.0.1:8080
```
Flow: Place order & freeze → review the generated brief with nine traffic-light checks →
settle. Tick **Fault injection** on the order page to watch a wrong price turn a light
red and void the authorization.

Offline checker:
```bash
python3 src/check.py examples/task.json examples/snapshot.json examples/generated.json
```

## PayPal sandbox evidence (verified 2026-10-09, test money only)
- Capture path: order APPROVED → `authorize` 201 → `capture` 201 **COMPLETED**
- Void path: order APPROVED → `authorize` 201 → `void` 204 → **VOIDED**

To wire live sandbox calls, copy `.env.example` values into environment variables
(`PAYPAL_CLIENT_ID`, `PAYPAL_CLIENT_SECRET`) from your own PayPal developer app.
Never commit credentials.

## Known gaps (honest scope for v1)
- Check 8 compares the generated amount against the task amount locally; binding it to a
  live PayPal order receipt is the next step, not yet verified.
- Task-id uniqueness across tasks and generator-version authenticity rely on self-reported
  values in this demo; no trusted execution log yet.
- The web demo runs the payment state machine in demo mode, mirroring the sandbox
  responses verified above. The two are separate: demo runs move no money.

## Reuse
Data snapshot format comes from the PriceScout price-feed pipeline; the nine-check
framework generalises the rule-gate pattern used in our opportunity-scanning systems.

License: MIT (see LICENSE).

Third-party and reuse declarations: see THIRD-PARTY-NOTICES.md.
