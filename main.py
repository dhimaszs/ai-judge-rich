import os

PLAN = """Plan: earn only from posted-price, escrow-backed coding work. No cold pitches, no unpaid trials.
Day 1: set up a Solana wallet and GitHub account, list the live priced work: DevPool lists 89 priced issues ($31,910 posted, 79 unassigned, $29,135); make.fun lists 11 open bounties. Take only work with a posted price, a published acceptance test, and a one-day fix.
Daily: claim at most 2 issues, reproduce the bug with a failing test, fix it, prove it with the repo's tests, PR within 24 hours. Drop anything stalled over 5 days. Between code tasks, enter make.fun bounties with a published judge prompt; draft several, submit only the best.
Money: DevPool paid $178,068 over 669 priced tasks, about $266 each. Base: attempt 12 issues, half pay, 6 x $300 = $1,800, plus one $100 make.fun win. Floor: only a quarter pay, 3 x $300 = $900, no wins. Stop rule: drop any bounty type that pays nothing after 3 tries. Fees about $10. Day 30 base: $100 + $1,800 + $100 - $10 = about $1,990; floor about $990."""

out = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out, exist_ok=True)
with open(os.path.join(out, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PLAN)
