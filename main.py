import os
PLAN = """Plan: turn scanned PDF invoices into bookkeeper-ready CSVs, by code, 24/7.
Day 1: build a one-page site: "PDF invoices to clean CSV, $29 per 50 pages, paid upfront by Stripe link, delivered in 2 hours." List 200 small US bookkeeping firms from Google Maps, take the contact email on each firm's own site, email the first 30 offering a free 10-page sample.
Days 2-30: email 30 new firms a day. Parse PDFs with Python, reconcile every invoice total against its line items, deliver the CSV plus a one-page exception report listing every mismatch and unreadable page, same day.
Why it wins: bookkeepers pay for accuracy they can audit, not just speed. A human skips the check; my code checks 100% of totals and never sleeps, so firms trust the file and come back.
Money: 900 emails, 3% reply, 12 trials, 6 pay $29 ($174) and 3 of them sign a $99/month retainer for 200 pages, paid upfront ($297). Revenue $471, Stripe fees ~$14, no ads. Day 30: $100 + $471 - $14 = about $557."""
os.makedirs(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), exist_ok=True)
open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"), "w", encoding="utf-8").write(PLAN)
