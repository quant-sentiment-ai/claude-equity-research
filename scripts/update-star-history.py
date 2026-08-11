#!/usr/bin/env python3
"""Regenerate the star-history data file and chart.

GitHub restricted /stargazers to repo admins and collaborators on 2026-06-30,
so star-history.com can no longer render this repo's chart from its own
servers. This script pulls the data with a token that *does* have access and
commits a static SVG instead.

Usage:
    gh auth status                       # must be a repo admin or collaborator
    python3 scripts/update-star-history.py

Writes:
    .github/star-history/stars.json      cumulative series, one point per day
    .github/star-history/chart.svg       rendered chart embedded in README.md
"""

import json
import subprocess
import sys
from collections import Counter
from datetime import date, datetime, timedelta
from pathlib import Path

REPO = "quant-sentiment-ai/claude-equity-research"
ROOT = Path(__file__).resolve().parent.parent
DATA = ROOT / ".github" / "star-history" / "stars.json"
CHART = ROOT / ".github" / "star-history" / "chart.svg"

W, H = 800, 400
PAD_L, PAD_R, PAD_T, PAD_B = 70, 30, 30, 50

# Chosen to stay legible on both the light and dark GitHub themes. GitHub
# proxies README images through camo, which strips <style> media queries, so a
# single theme-neutral palette is the only thing that reliably works.
LINE = "#2f81f7"
FILL = "#2f81f7"
AXIS = "#8b949e"
TEXT = "#8b949e"


def fetch_starred_at() -> list[str]:
    """Every starred_at timestamp, oldest first."""
    out = subprocess.run(
        [
            "gh", "api", f"repos/{REPO}/stargazers?per_page=100",
            "-H", "Accept: application/vnd.github.star+json",
            "--paginate", "--jq", ".[].starred_at",
        ],
        capture_output=True, text=True,
    )
    if out.returncode != 0:
        sys.exit(
            f"Failed to read stargazers: {out.stderr.strip()}\n\n"
            "A 401/403/404 here means the token isn't an admin or collaborator "
            "on the repo. See github-stargazer-api-restriction."
        )
    stamps = [line for line in out.stdout.splitlines() if line]
    if not stamps:
        sys.exit("Stargazers call succeeded but returned nothing — refusing to "
                 "overwrite the existing chart with an empty series.")
    return sorted(stamps)


def to_daily_series(stamps: list[str]) -> list[tuple[str, int]]:
    per_day = Counter(s[:10] for s in stamps)
    start = date.fromisoformat(min(per_day))
    end = date.fromisoformat(max(per_day))
    series, running = [], 0
    day = start
    while day <= end:
        running += per_day.get(day.isoformat(), 0)
        series.append((day.isoformat(), running))
        day += timedelta(days=1)
    return series


def nice_axis(n: int) -> tuple[int, int]:
    """Return (ceiling, divisions) for the tightest round y-axis clearing n.

    Picking the ceiling directly (100/200/500/1000...) strands the line low in
    the plot — 687 would round to 1000 and waste a third of the height.
    Rounding the *step* instead gives 200 x 4 = 800. Trying both 4 and 5
    gridlines and keeping the tighter result stops mid-range totals from
    getting a loose axis (1200 -> 1250 with 5 lines, not 2000 with 4).
    """
    best = None
    for divisions in (4, 5):
        target = n / divisions
        magnitude = 10 ** max(len(str(int(target))) - 1, 0)
        for mult in (1, 2, 2.5, 5, 10):
            step = magnitude * mult
            if step >= target:
                ceiling = int(step * divisions)
                if best is None or ceiling < best[0]:
                    best = (ceiling, divisions)
                break
    return best or (n, 4)


def render(series: list[tuple[str, int]]) -> str:
    total = series[-1][1]
    y_max, divisions = nice_axis(total)
    plot_w = W - PAD_L - PAD_R
    plot_h = H - PAD_T - PAD_B

    def x_of(i: int) -> float:
        return PAD_L + (plot_w * i / max(len(series) - 1, 1))

    def y_of(v: int) -> float:
        return PAD_T + plot_h - (plot_h * v / y_max)

    pts = " ".join(f"{x_of(i):.1f},{y_of(v):.1f}" for i, (_, v) in enumerate(series))
    area = f"{PAD_L},{PAD_T + plot_h:.1f} {pts} {x_of(len(series) - 1):.1f},{PAD_T + plot_h:.1f}"

    parts = [
        f'<svg xmlns="http://www.w3.org/2000/svg" width="{W}" height="{H}" '
        f'viewBox="0 0 {W} {H}" role="img" aria-label="Star history: {total} stars">',
        f'<title>Star history — {total} stars</title>',
    ]

    # horizontal gridlines + y labels
    for i in range(divisions + 1):
        v = int(y_max * i / divisions)
        y = y_of(v)
        parts.append(
            f'<line x1="{PAD_L}" y1="{y:.1f}" x2="{W - PAD_R}" y2="{y:.1f}" '
            f'stroke="{AXIS}" stroke-width="1" stroke-opacity="0.25"/>'
        )
        parts.append(
            f'<text x="{PAD_L - 10}" y="{y + 4:.1f}" text-anchor="end" '
            f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" '
            f'font-size="12" fill="{TEXT}">{v}</text>'
        )

    # month ticks
    seen = set()
    for i, (d, _) in enumerate(series):
        month = d[:7]
        if month in seen or d[8:10] != "01":
            continue
        seen.add(month)
        label = datetime.strptime(month, "%Y-%m").strftime("%b %Y")
        parts.append(
            f'<text x="{x_of(i):.1f}" y="{H - PAD_B + 22}" text-anchor="middle" '
            f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" '
            f'font-size="11" fill="{TEXT}">{label}</text>'
        )

    parts += [
        f'<polygon points="{area}" fill="{FILL}" fill-opacity="0.12"/>',
        f'<polyline points="{pts}" fill="none" stroke="{LINE}" stroke-width="2.5" '
        f'stroke-linejoin="round" stroke-linecap="round"/>',
        f'<circle cx="{x_of(len(series) - 1):.1f}" cy="{y_of(total):.1f}" r="4" fill="{LINE}"/>',
        f'<text x="{W - PAD_R}" y="{PAD_T - 8}" text-anchor="end" '
        f'font-family="-apple-system,BlinkMacSystemFont,Segoe UI,Helvetica,Arial,sans-serif" '
        f'font-size="13" font-weight="600" fill="{LINE}">{total} stars</text>',
        f'<line x1="{PAD_L}" y1="{PAD_T + plot_h:.1f}" x2="{W - PAD_R}" y2="{PAD_T + plot_h:.1f}" '
        f'stroke="{AXIS}" stroke-width="1" stroke-opacity="0.5"/>',
        "</svg>",
    ]
    return "\n".join(parts)


def main() -> None:
    stamps = fetch_starred_at()
    series = to_daily_series(stamps)
    DATA.parent.mkdir(parents=True, exist_ok=True)
    DATA.write_text(json.dumps(
        {
            "repo": REPO,
            "generated_from": "GET /repos/{owner}/{repo}/stargazers (collaborator access)",
            "total": series[-1][1],
            "first_star": stamps[0],
            "last_star": stamps[-1],
            "series": [{"date": d, "stars": v} for d, v in series],
        },
        indent=2,
    ) + "\n")
    CHART.write_text(render(series) + "\n")
    print(f"{len(stamps)} stars · {series[0][0]} → {series[-1][0]}")
    print(f"wrote {DATA.relative_to(ROOT)} and {CHART.relative_to(ROOT)}")


if __name__ == "__main__":
    main()
