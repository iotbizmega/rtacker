# Instructions for GitHub Copilot

This repo is a Persian (RTL) fleet-tracking **demo** ("سامانه رهگیری و مدیریت ناوگان") being turned into a real system. Read `CLAUDE.md`, `README.md`, `docs/ARCHITECTURE.md`, `docs/ROADMAP.md`, `docs/DEMO_VS_REAL.md` first.

- Demo code: `src/template.html`, `src/live.js`; build with `python3 build.py` (output `dist/`, never commit it).
- Before finishing any task run: `python3 build.py && pip install -r requirements-dev.txt && python -m playwright install chromium && python tests/smoke.py` — it must pass.
- UI language is Persian, right-to-left, Persian digits in tables, Jalali dates; keep vehicle/channel IDs Latin (`102 [جلو]`). Keep the menu order unchanged.
- Never present simulated data as real; document every mock in `docs/DEMO_VS_REAL.md`.
- No secrets, tokens or credentials in the repo. Do not add third-party media of unknown license.
- Work in small PRs, one roadmap phase item per PR. Write the plan and open questions in the PR description. If a requirement is unclear (device protocol, hosting, stack), ask in the issue instead of guessing.
- Do not delete the demo until the new app reaches feature parity; move it to `legacy-demo/` only when an issue says so.
