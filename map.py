import geopandas as gpd
import pandas as pd
import matplotlib.pyplot as plt

url = "https://services1.arcgis.com/ESMARspQHYMw9BZ9/arcgis/rest/services/Local_Authority_Districts_December_2024_Boundaries_UK_BUC/FeatureServer/0/query?where=1=1&outFields=*&f=geojson"

print("Downloading boundaries...")
gdf = gpd.read_file(url)

targets = ["Breckland", "Broadland", "Great Yarmouth",
           "King's Lynn and West Norfolk", "North Norfolk",
           "Norwich", "South Norfolk"]
norfolk = gdf[gdf["LAD24NM"].isin(targets)].copy()

counts = pd.read_csv("norfolk_district_counts.csv")

merged = norfolk.merge(counts, left_on="LAD24NM", right_on="district", how="left")

print("Merged table:")
print(merged[["LAD24NM", "coin_count"]])

fig, ax = plt.subplots(1, 1, figsize=(9, 10))
merged.plot(
    column="coin_count",
    cmap="YlOrRd",
    linewidth=0.6,
    edgecolor="0.4",
    legend=True,
    legend_kwds={"label": "Number of Roman coin finds", "shrink": 0.6},
    ax=ax,
)

for idx, row in merged.iterrows():
    ax.annotate(
        text=row["LAD24NM"],
        xy=(row.geometry.centroid.x, row.geometry.centroid.y),
        ha="center", fontsize=7, color="black",
    )

ax.set_title("Norfolk: Roman coin finds per district (PAS data)", fontsize=13)
ax.axis("off")

plt.savefig("norfolk_choropleth.png", dpi=150, bbox_inches="tight")
print("Saved: norfolk_choropleth.png")
plt.show()
