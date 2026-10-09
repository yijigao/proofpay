# Hosted demo plan (for the Judging Period 2026-12-01 → 12-15)

**Correction (2026-10-09, per dispatch-desk precheck):** Hugging Face *Docker*
Spaces require a paid plan — the earlier "free, no card" assumption was wrong.
The hosting route is therefore **pending Joey's decision**; options:

| Option | Cost | Card | Notes |
|---|---|---|---|
| HF Spaces (Docker) | paid plan required | likely | Clean public URL, auto rebuild from repo |
| HF Spaces (Gradio/static workarounds) | free tier exists | no | Needs app rework to fit non-Docker SDK |
| Render free web service | free tier | no card for free tier | Spins down ~15 min idle, cold start ~1 min |
| Own VPS (tokyo-edge, already paid) | $0 marginal | n/a | Always-on; needs port/domain care by 烛龙 |

Whatever the route, the app now binds `0.0.0.0:$PORT` and builds demo fixtures
relative to the current time, so freshness/deadline never expire in December.

## If HF Docker Space is chosen — repo metadata step
1. Create the Space (Docker SDK) from this repo under Joey's HF account.
2. In the **Space repo's README.md frontmatter** (Space repo only, not GitHub), set:
   ```yaml
   ---
   title: ProofPay
   sdk: docker
   app_port: 7860
   ---
   ```
3. Space builds `Dockerfile` (`python3 src/app.py`, PORT=7860) and serves the
   three pages publicly.

## Four answers (any route)
- **Startup**: container/process runs `python3 src/app.py` on `0.0.0.0:$PORT`.
- **Temporary state**: task state is in-memory; restart resets the demo —
  every order is self-contained with a unique id, so concurrent judges don't
  overwrite each other.
- **Restart**: platform auto-restarts on crash; manual restart available.
- **Sleep / expiry**: free tiers sleep when idle and wake on first visit
  (cold start ~1 min); before judging we ping it awake (2026-11-30) and
  re-check weekly. No credentials are deployed anywhere.
