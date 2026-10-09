# Third-party & reuse notices

This repo is MIT-licensed (see LICENSE) for its own original code and docs.
The following clarifies every reused name, format, tool, and material so nothing
is silently re-licensed:

## Example data (G1, G7)
- `examples/*.json` are **fully synthetic sample data written for this demo**
  (generic product names, invented prices, `example.com` placeholder links).
  No scraped or third-party data is included, and no real buyer is referenced.
- "PriceScout feed format" means field-shape compatibility with the author's
  own PriceScout pipeline (`sku/title/price_old/price_new/currency/url/seen_at_utc`).
  No PriceScout code or data is copied into this repo.

## Rule-check framework (G2)
- The nine-check gate pattern is the author's own design, generalised from
  internal opportunity-scanning rules. `src/check.py` was written fresh for
  this project; no third-party code is vendored.

## Hackathon rules memo (G3)
- `RULES-MEMO.md` is our own summary of the official rules, with the source
  linked and dated. It is not a copy of the rules text and is not offered as
  MIT-licensed PayPal/Devpost material; the official page governs.

## Dev-only tooling (G4)
- `video/record.py` imports Playwright (Apache-2.0, Microsoft) as a local
  recording tool only. It is not vendored, bundled, or distributed; no browser
  binaries are in this repo.

## Runtime (G5)
- Python 3 standard library only (PSF License). The `Dockerfile` references
  the official `python:3.12-slim` image for optional hosting; the image and
  its components keep their own licenses and are not distributed from here.

## Trademarks & services (G6)
- PayPal, Devpost, YouTube, Hugging Face, and AI-tool names appear in
  nominative/descriptive use only (what the project integrates with). No
  logos, brand assets, SDKs, or screenshots of third-party services are in
  this repo. Each service's own terms apply to its use.

## Demo video (G8)
- The demo video contains only footage of this project's own UI, on-screen
  captions, and synthetic TTS narration. **No background music** and no
  third-party media are used. If music or external media is ever added, its
  title/author/source/license will be recorded here before publishing.
