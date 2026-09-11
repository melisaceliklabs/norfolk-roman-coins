"""
Norfolk Roman coins (PAS) — dataset overview.

Establishes the counting unit used throughout the project: a PAS record is
not always a single coin. The `quantity` field can exceed 1 where a record
covers a group or hoard, so record counts and coin counts diverge.

Run:  python 01_data_overview.py
"""

import pandas as pd

CSV = "norfolk-finds.csv"

# The PAS export is cp1252/latin-1, not utf-8. Reading it as utf-8 raises
# UnicodeDecodeError on byte 0xb7. All non-ASCII bytes in this file sit in
# the range where latin-1 and cp1252 agree, so either is safe here.
df = pd.read_csv(CSV, encoding="latin-1", low_memory=False)

assert df["id"].is_unique, "Duplicate record ids in export"
assert df["quantity"].notna().all(), "Null quantity values"

records = len(df)
coins = int(df["quantity"].sum())
multi = df[df["quantity"] > 1]

print("=== Counting unit ===")
print(f"Records                : {records:,}")
print(f"Coins (sum of quantity): {coins:,}")
print(f"Difference             : {coins - records:,}")
print(f"Multi-coin records     : {len(multi):,} ({len(multi) / records:.1%})")
print(f"Coins in those records : {int(multi['quantity'].sum()):,}")
print(f"Largest single record  : {int(df['quantity'].max())} coins")

# Robustness check: does the counting unit change the spatial picture?
by_district = (
    df.dropna(subset=["district"])
    .groupby("district")
    .agg(records=("id", "size"), coins=("quantity", "sum"))
)

rank_records = by_district.sort_values("records", ascending=False).index.tolist()
rank_coins = by_district.sort_values("coins", ascending=False).index.tolist()

print("\n=== District counts, both units ===")
print(by_district.sort_values("records", ascending=False).to_string())
print(f"\nDistrict ranking identical under both units: {rank_records == rank_coins}")

missing_district = df["district"].isna().sum()
if missing_district:
    print(f"\nRecords with no district assigned: {missing_district} (excluded above)")
