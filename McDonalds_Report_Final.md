# McDonald's Stores Dataset — Analysis Report (Final)

Generated: 2025-10-06T13:58:15.865247Z

## 1. Introduction
This analysis inspects McDonald's store location data (columns, counts, coordinates). It includes cleaning, EDA, and visualizations.

## 2. Data Understanding
- Rows (after dropping rows with no coordinates): 39195
- Columns: 12

### Column descriptions
- **name**: Restaurant name (usually 'McDonald's' or specific store name).
- **storeid**: Unique store identifier (ID).
- **country**: Country where the store is located.
- **subdivision**: State, province, or region within the country.
- **city**: City of the store.
- **address**: Street address of the store.
- **postcode**: Postal code / ZIP code (kept as string because formats vary).
- **telephone**: Store phone number.
- **runhours**: Operating hours or schedule for the store.
- **latitude**: Latitude coordinate (float).
- **longitude**: Longitude coordinate (float).
- **services**: Services offered (e.g., Drive-Thru, Delivery, Takeaway) — may be a string listing services.

## 3. Cleaning Summary
- missing_counts: {'services': 9, 'name': 0, 'storeid': 0, 'country': 0, 'subdivision': 0, 'city': 0, 'address': 0, 'postcode': 0, 'telephone': 0, 'runhours': 0, 'latitude': 0, 'longitude': 0}
- dropped_rows_no_coords: 0
- filled_services: Filled 9 missing with 'Unknown'.
- duplicates_found: 0
- duplicates_removed: 0
- coordinate_outlier_checks: {'latitude': {'count_out_of_realistic_bounds': 0, 'min': -46.4207179, 'max': 68.970545}, 'longitude': {'count_out_of_realistic_bounds': 0, 'min': -171.7687002, 'max': 178.4467715}}

## 4. EDA — Key snapshots
### Numeric summary (latitude, longitude)
|           |   count |     mean |     std |       min |      25% |      50% |      75% |      max |
|:----------|--------:|---------:|--------:|----------:|---------:|---------:|---------:|---------:|
| latitude  |   39195 | 32.0415  | 20.8792 |  -46.4207 |  28.6039 | 36.4482  |  43.8909 |  68.9705 |
| longitude |   39195 |  7.66213 | 90.8186 | -171.769  | -81.4302 |  5.09055 | 113.414  | 178.447  |

### Top countries (by store count)
|                |   country |
|:---------------|----------:|
| United States  |     12419 |
| China          |      5906 |
| Japan          |      2963 |
| France         |      1597 |
| United Kingdom |      1416 |
| Germany        |      1416 |
| Canada         |      1408 |
| Brazil         |      1052 |
| Australia      |      1014 |
| Russia         |       863 |
| Italy          |       674 |
| Philippines    |       654 |
| Poland         |       531 |
| India          |       407 |
| South Korea    |       403 |
| Malaysia       |       348 |
| Spain          |       347 |
| South Africa   |       341 |
| Indonesia      |       297 |
| Netherlands    |       270 |

## 5. Visualizations
Plots saved in `/mnt/data/plots_mcd_final/`:
- bar_top_countries.png
- boxplot_latitude.png
- heatmap_latlon.png
- hist_latitude.png
- line_top_subdivisions.png
- pie_top6_countries.png

## 6. Key insights
- The country with most stores in the dataset is 'United States' with 12419 stores.
- Average latitude: 32.0415, average longitude: 7.6621.
- Top 5 cities by store count:
北京市    422
上海市    422
深圳市    341
大津市    341
广州市    309
- Top services entries (most common):
McDrive/Giftcards/Linkedpay/Loyalty/McDelivery/MobileDeals/WiFi              5511
McDrive/Giftcards/Linkedpay/Loyalty/McDelivery/MobileDeals/24Hours/WiFi      2225
McDrive/Giftcards/Linkedpay/Loyalty/McDelivery/MobileDeals/Partyroom/WiFi    1594
nodata                                                                       1200
McCafé                                                                        873

## 7. Conclusion
This dataset is primarily geographic/store-location oriented. Use these insights for mapping, regional analysis, or combining with sales/nutrition datasets for deeper business intelligence.
