import os

PLAN = """Plan: turn scanned PDF invoices into clean CSVs for bookkeepers, code only, 24/7.
Day 1: one page: "PDF invoices to clean CSV, $29 per 50 pages, pay upfront via Stripe link, back in 2 hours." Find 200 small US bookkeeping firms on Google Maps, take each contact email from its own site, email the first 30, 10 pages free.
Days 2-30: email 30 new firms daily, and follow up once with any firm that opened the email but did not reply. Parse PDFs in Python, reconcile every total with its line items, deliver the CSV plus a one-page mismatch and unreadable-page report, same day.
Edge: bookkeepers pay for numbers they can audit, not speed alone. Humans skip the check; my code checks every total and never sleeps, so firms trust it, return, and hand over repeat work.
Money: 900 emails, ~3% reply, 12 trials, 6 pay $29 ($174), 3 sign a $99/month retainer for 200 pages upfront ($297). Revenue $471, Stripe ~$14, no ads. Day 30: $100 + $471 - $14 = about $557."""

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
    f.write(PLAN)
