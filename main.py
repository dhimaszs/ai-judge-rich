import os
PLAN = """Plan: turn scanned PDF invoices into bookkeeper-ready CSVs, by code, 24/7.
Day 1: one-page site: "PDF invoices to clean CSV, $29 per 50 pages, paid upfront by Stripe link, delivered in 2 hours." Post in r/bookkeeping, QuickBooks forums, and Upwork jobs from the last 24 hours. First 5 pages free as a sample.
Days 2-7: take every job. Parse PDFs with Python, check totals against the PDF, fix mismatches by hand, deliver the same day. Ask each buyer for a review and one referral.
Days 8-30: raise price to $39 after 10 paid jobs. Spend $60 on ads only after 5 jobs come from one channel. Offer $99/month for 200 pages to the best 3 buyers.
Why it wins: bookkeepers already pay for this daily, have repeat volume, and hate manual entry. A human takes 3 hours per 50 pages; my code takes 20 minutes, so I undercut on price, deliver same day, and work while humans sleep. Drop any channel with no paying buyer in 5 days.
Expected: 15-20 paid jobs by day 30, about $500-600 kept, not a lottery ticket."""
os.makedirs(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), exist_ok=True)
open(os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.txt"), "w", encoding="utf-8").write(PLAN)
