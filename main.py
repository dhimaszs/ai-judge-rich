"""Write the ai-judge-rich-01 entry plan to entry.txt.

Deterministic, no network. Reads MAKEFUN_OUTPUT_DIR if set,
otherwise writes to /output/entry.txt.
"""

import hashlib
import os


PLAN = (
    "Judge: escrowed money only; read the judge prompt. "
    "$100, computer, internet, 30 days, no human help; "
    "most dollars day 30.\n"
    "Top earner $570.50, 20/25 paid ($22.82 each); "
    "top-50 avg $6.35; 7 open; 844 paid since Nov 9.\n"
    "No: cold email unread; Fiverr/Upwork/Stripe need ID; "
    "Gitcoin shut; DevPool rarely merges outsider PRs.\n"
    "Split $100: $30 credit, $30 fees, $40 reserve. "
    "Day 1: wallet + key, file 3 free pots closing soonest, "
    "settling before day 30.\n"
    "Per entry: read the judge prompt, write 4 drafts, duel all 4 "
    "both orders, duel winner vs top 5; file only board-beaters.\n"
    "Pace 3/day, 5 once USDC wins recycle into fees/credit. "
    "Morning board check; pick by settlement.\n"
    "120 entries, 100 settle at half-leader rate $11.41 = $1,141; "
    "day 30 $40 + $1,141 = $1,181. "
    "Floor: 100 at $6.35 = $635; day 30 $675.\n"
    "Stop: unpaid after 3 tries, type dropped; "
    "slots re-duel and re-file losers.\n"
    "Edge vs 1,000 lookalikes: they file blind, chase prizes. "
    "Files board-beating drafts, picks by settlement, "
    "recycles wins."
)


def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(PLAN)
    print(f"wrote {path}: {len(PLAN)} chars, "
          f"sha256 {hashlib.sha256(PLAN.encode('utf-8')).hexdigest()}")


if __name__ == "__main__":
    main()
