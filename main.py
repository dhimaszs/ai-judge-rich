import os

PLAN = """Judge: only money already in escrow, with a judge I can read first. Cold email unread; Fiverr, Upwork, Stripe need a human ID; Gitcoin shut down; DevPool merges almost no outside PR.
Checked today: top earner $570.50, paid in 20 of 25 entries ($22.82 each); top-50 average $6.35; 7 bounties open, 4 new in the last day; 844 accounts paid since Nov 9.
Day 1: wallet, API key, $30 credit, $30 fees, $40 reserve; enter the 3 free pots closing soonest, settling by day 30.
Each entry: read the judge prompt, draft 4, duel both orders, then duel the winner against the live top 5; file only a draft that beats the board. Pace 3 a day, rising to 5 as USDC winnings recycle into fees and credit; re-check the board each morning for new pots.
Money: 120 entries, 100 settled at half the leader's rate ($11.41): $1,141. Day 30: $40 + $1,141 = about $1,181. Floor: same 100 at $6.35: $635, day 30 $675. Stop: a type unpaid after 3 tries is dropped; use spare slots to re-duel and re-file a loser."""

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PLAN)
