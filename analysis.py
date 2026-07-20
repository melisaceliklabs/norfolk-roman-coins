import pandas as pd
import matplotlib.pyplot as plt

path = "norfolk-finds.csv"
df = pd.read_csv(path, encoding="latin-1", low_memory=False)

top_rulers = df["rulerName"].value_counts().head(12).sort_values()
fig, ax = plt.subplots(figsize=(9, 6))
top_rulers.plot(kind="barh", color="#8c1d1d", ax=ax)
ax.set_title("Norfolk Roman coins: most common rulers (PAS data)")
ax.set_xlabel("Number of coins")
plt.tight_layout()
plt.savefig("rulers.png", dpi=150)
print("Saved rulers.png")

top_denom = df["denominationName"].value_counts().head(12).sort_values()
fig, ax = plt.subplots(figsize=(9, 6))
top_denom.plot(kind="barh", color="#1d5c8c", ax=ax)
ax.set_title("Norfolk Roman coins: denominations (PAS data)")
ax.set_xlabel("Number of coins")
plt.tight_layout()
plt.savefig("denominations.png", dpi=150)
print("Saved denominations.png")

dates = df["fromdate"].dropna()
dates = dates[(dates >= -250) & (dates <= 450)]
fig, ax = plt.subplots(figsize=(10, 5))
ax.hist(dates, bins=28, color="#8c1d1d", edgecolor="white")
ax.set_title("Norfolk Roman coins: chronological distribution by start date (PAS data)")
ax.set_xlabel("Year (negative = BC)")
ax.set_ylabel("Number of coins")
plt.tight_layout()
plt.savefig("chronology.png", dpi=150)
print("Saved chronology.png")

plt.show()
