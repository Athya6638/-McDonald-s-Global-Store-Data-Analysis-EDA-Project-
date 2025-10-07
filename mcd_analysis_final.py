
# McDonalds dataset analysis script (final)
# Run in a Jupyter/CPython environment. Requires pandas, numpy, matplotlib.
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
from datetime import datetime

FILEPATH = "/mnt/data/McDonalds.csv"
PLOT_DIR = "/mnt/data/plots_mcd_final"
os.makedirs(PLOT_DIR, exist_ok=True)

# Load dataset
df = pd.read_csv(FILEPATH)

# Data understanding
print("Shape:", df.shape)
print("Columns:", df.columns.tolist())
print(df.head())

# Column explanations (manual)
column_explanations = {
    "name": "Restaurant name",
    "storeid": "Unique store identifier",
    "country": "Country where store is located",
    "subdivision": "State/province/region",
    "city": "City of the store",
    "address": "Street address",
    "postcode": "Postal code (string)",
    "telephone": "Phone number",
    "runhours": "Operating hours",
    "latitude": "Latitude (float)",
    "longitude": "Longitude (float)",
    "services": "Services list (string)"
}

# Data cleaning
# Drop rows missing both coordinates
df = df.dropna(subset=['latitude','longitude'], how='all')
# Fill some non-critical missing values with 'Unknown'
for col in ['telephone','runhours','address','postcode','services']:
    if col in df.columns:
        df[col] = df[col].fillna("Unknown")

# Remove duplicates
df = df.drop_duplicates().reset_index(drop=True)

# Ensure dtypes
if 'storeid' in df.columns:
    df['storeid'] = df['storeid'].astype(str)
df['latitude'] = pd.to_numeric(df['latitude'], errors='coerce')
df['longitude'] = pd.to_numeric(df['longitude'], errors='coerce')

# EDA: summaries
print(df[['latitude','longitude']].describe())
print("Top countries:\n", df['country'].value_counts().head(10))
print("Top cities:\n", df['city'].value_counts().head(10))
print("Top services:\n", df['services'].value_counts().head(10))

# Visualizations (matplotlib)
def save_plot(fig, name):
    path = os.path.join(PLOT_DIR, name)
    fig.savefig(path, bbox_inches='tight')
    plt.close(fig)
    print("Saved:", path)

# Bar: top 10 countries
if 'country' in df.columns:
    top_countries = df['country'].value_counts().head(10)
    fig = plt.figure(figsize=(8,5))
    top_countries.plot(kind='bar')
    plt.title("Top 10 countries by number of McDonald's stores")
    plt.xlabel("Country")
    plt.ylabel("Store count")
    save_plot(fig, "bar_top_countries.png")

# Histogram: latitude
fig = plt.figure(figsize=(8,5))
df['latitude'].plot(kind='hist', bins=30)
plt.title("Distribution of store latitudes")
plt.xlabel("Latitude")
plt.ylabel("Frequency")
save_plot(fig, "hist_latitude.png")

# Pie: top 6 countries
if 'country' in df.columns:
    top6 = df['country'].value_counts().head(6)
    fig = plt.figure(figsize=(6,6))
    top6.plot(kind='pie', autopct='%1.1f%%', ylabel='')
    plt.title("Top 6 countries share (by store count)")
    save_plot(fig, "pie_top6_countries.png")

# Line: subdivisions (top 15)
if 'subdivision' in df.columns:
    subdiv_top = df['subdivision'].value_counts().head(15).sort_values(ascending=True)
    fig = plt.figure(figsize=(10,4))
    subdiv_top.plot(kind='line', marker='o')
    plt.title("Top 15 subdivisions by store count (line plot)")
    plt.xlabel("Subdivision (top 15)")
    plt.ylabel("Store count")
    plt.xticks(rotation=45, ha='right')
    save_plot(fig, "line_top_subdivisions.png")

# Heatmap: lat/lon correlation (imshow)
corr = df[['latitude','longitude']].corr()
fig = plt.figure(figsize=(5,4))
plt.imshow(corr, aspect='auto')
plt.colorbar()
plt.xticks(ticks=np.arange(len(corr.columns)), labels=corr.columns, rotation=45)
plt.yticks(ticks=np.arange(len(corr.index)), labels=corr.index)
plt.title("Correlation heatmap (lat, lon)")
save_plot(fig, "heatmap_latlon.png")

# Boxplot: latitude
fig = plt.figure(figsize=(8,3))
plt.boxplot(df['latitude'].dropna(), vert=False)
plt.title("Boxplot of latitude (outlier visualization)")
save_plot(fig, "boxplot_latitude.png")

# Save cleaned CSV
cleaned_path = "/mnt/data/McDonalds_cleaned_final.csv"
df.to_csv(cleaned_path, index=False)
print("Cleaned CSV saved to:", cleaned_path)
