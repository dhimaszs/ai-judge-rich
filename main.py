import os

PLAN = """Judge: only posted money held in escrow, with a readable judge first. Cold email unread; Fiverr, Upwork, Stripe need a human ID; Gitcoin shut down; DevPool merged almost no outside PR.
Checked today: top earner $570.50, 20 of 25 ($22.82 each); top-50 average $6.35; 4 new bounties a day. DevPool: 79 unassigned issues, median $150, $178,068 paid over 669 tasks.
Day 1: wallet, API key, $20 credit, $10 fees, $70 reserve; enter 3 newest free pots settling by day 30.
Daily: read the judge prompt, draft 4, duel both orders, file the winner; check top-5 scores, enter only beatable pots; 3 a day rising to 5 as winnings recycle. DevPool in spare hours: outside PR merged in 7d, green CI, issue unassigned, max 2 claims, PR in 24h, drop stalled in 5 days.
Money: 120 entries, 100 settled at half the leader's rate ($11.41): $1,141, plus 3 DevPool merges at $150: $450. Day 30: $70 + $1,141 + $450 = $1,661. Floor: same 100 at $6.35: $635, day 30 $705. Stop: unpaid after 3 tries, drop the type."""

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PLAN)
