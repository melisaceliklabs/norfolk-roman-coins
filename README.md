# norfolk-roman-coins
Spatial and numismatic analysis of Roman coin finds from Norfolk (PAS data)
# Norfolk Roman Coin Finds — a spatial and numismatic analysis

A self-directed data project analysing Roman coin finds from Norfolk, England, as recorded by the Portable Antiquities Scheme (PAS). It combines archaeological domain knowledge with spatial-data and analysis tooling.

## Data
- **Source:** Portable Antiquities Scheme (finds.org.uk), public database export
- **Scope:** 25,394 individual Roman coin records from Norfolk
- **Note on location:** the public export restricts findspot data below county level — precise coordinates are deliberately withheld to protect sites from illicit metal-detecting. Spatial analysis here is therefore at district level. Finer (1 km grid) references require a PAS research account.

## Tools
Python (pandas, GeoPandas), matplotlib, and ONS district boundaries from the Open Geography Portal.

## What the data shows
- **Spatial:** finds concentrate in the rural western and central districts (Breckland, King's Lynn and West Norfolk); the urban district of Norwich records almost none.
- **Chronological:** coin loss rises sharply from the mid-3rd century AD, peaking under the House of Constantine (early-to-mid 4th century).
- **Denominations:** dominated by late-Roman low-value bronze (nummi, radiates), consistent with the chronology.

## An important caveat
This distribution reflects modern recovery, not ancient reality. Small late-Roman bronzes survive well in ploughsoil and are easily found by metal-detectorists; the near-absence of finds in Norwich reflects modern urban land use, not Roman activity. The dataset is shaped by the recording process itself.

## Figures
| File | Shows |
|------|-------|
| `norfolk_choropleth.png` | Coin finds per district |
| `rulers.png` | Most common rulers |
| `denominations.png` | Denomination breakdown |
| `chronology.png` | Chronological distribution |

## Next steps
- Obtain PAS research access for 1 km grid references, enabling point-level mapping
- Model graduated findspot access control (row-level security) as a data-governance layer
