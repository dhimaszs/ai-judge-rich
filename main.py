import os

PLAN = """Plan: turn scanned PDF invoices into tidy CSVs bookkeepers can use, done by code alone, day and night.
Day 1: build one page: "Scanned PDF invoices to clean CSV, $29 per 50 pages, pay upfront by Stripe link, back in 2 hours." List 200 small US bookkeeping firms on Google Maps, take each firm's contact email from its own site, and email the first 30 with 10 pages free.
Days 2-30: write to 30 fresh firms every day. Read PDFs in Python, check every invoice total against its line items, and send the CSV plus a one-page list of mismatches and unreadable pages, same day.
Why it wins: bookkeepers pay for figures they can check, not just speed. People skip the checking; my code checks every total and never sleeps, so firms trust the file and come back.
Money: 900 emails, about 3% answer, 12 try it, 6 pay $29 ($174), 3 take a $99-a-month retainer for 200 pages, paid upfront ($297). Sales $471, Stripe about $14, no ads. Day 30: $100 + $471 - $14 = about $557."""

outdir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(outdir, exist_ok=True)
with open(os.path.join(outdir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PLAN)
