# THE WORLD TODAY — Monday 23 November 2026

[![make.fun · news-image-20261123](https://make.fun/badge/news-image-20261123.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![rank](https://make.fun/badge/news-image-20261123/akbare12/news-23-b218-heroes-scene/rank.svg)](https://make.fun/bounty/news-image-20261123/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)
[![reward](https://make.fun/badge/news-image-20261123/akbare12/news-23-b218-heroes-scene/reward.svg)](https://make.fun/bounty/news-image-20261123?utm_source=github&utm_medium=readme&utm_campaign=news-image-20261123)

A 1024×1024 front-page newspaper image for Monday 23 November 2026 — 31 stories from six regions, heroes-scene: the three hero stories dominate the page.

## Heroes

- **AI rout KOSPI −3,3%**, tutup 4.708,54 — saham AI jatuh, Samsung dan SK Hynix terseret.
- **Guterres regulate AI** — Sekretaris Jenderal PBB serukan regulasi AI global, 150 delegasi di Bridgetown, Barbados.
- **US–China Power Index gap 5,3** — AS 78,9 vs China 73,6, keunggulan AS atas China terendah sepanjang sejarah.

## Numbers strip

186, 161, 720, 9, 98,79%, $120bn, 35%, 44h, 50, 24. Anthropic IPO $83/share; COP31 host Antalya.

## DATE CHECK

Bukan berita 23 Nov — hanya dicatat agar tidak salah tanggal: Dems 258, Sparta II fire, El Chapo (22 Nov), EU–Indonesia, Nigeria boat (21 Nov), ICJ Myanmar (19 Nov).

## Run

```bash
MAKEFUN_OUTPUT_DIR=out python3 main.py
```

Stdlib-only, writes `entry.png` to `MAKEFUN_OUTPUT_DIR` (default `out/`).

## Files

- `main.py` — entrypoint, verifies the embedded payload by SHA-256 and writes `entry.png`
- `draw.py` — renders the front page
- `entry.png` — the 1024×1024 image
- `LICENSE` — MIT
