# Hosted demo plan (for the Judging Period 2026-12-01 → 12-15)

Chosen: **Hugging Face Spaces (Docker, free CPU tier)** — free, no credit card,
public URL, judges need no account.

Four answers the reviewers asked for:
- **Startup**: Space builds the repo Dockerfile (`python3 src/app.py`, PORT=7860)
  and serves the same three pages as the local demo; env `PORT` respected.
- **Temporary state**: task state is in-memory by design; a restart simply resets
  the demo (no data worth keeping; every run is self-contained).
- **Restart**: Spaces auto-restarts the container on crash; manual restart from
  the Space page. Local fallback in README always available.
- **Sleep / expiry**: free Spaces sleep after ~48h inactivity and wake on first
  visit (cold start under a minute). No expiry while the account is active;
  before the judging window we will ping it awake and verify. Upgrade to a paid
  always-on tier is optional and NOT required.

Pre-judging checklist (before 2026-12-01):
1. Create the Space from this repo (Joey's HF account, 5 minutes).
2. Verify the three pages complete both endings (capture + void) on the public URL.
3. Put the Space URL into README + Devpost "Try it out" before the 2026-11-12 deadline.
4. Wake-check the URL on 2026-11-30 and weekly during judging.

Note: the hosted demo runs the same local-demo state machine; live PayPal sandbox
evidence is the verified 2026-10-09 run documented in README. No credentials are
deployed to the Space.
