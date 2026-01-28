import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Global Overview 🌍")

# make sure data exists (important in multipage apps)
if "data" not in st.session_state:
    st.error("Data not loaded. Please open the main page first.")
    st.stop()

df = st.session_state.data.copy()

# -------------------------
# Year selection
# -------------------------
min_year = int(df["year"].min())
max_year = int(df["year"].max())

year = st.slider("Year", min_year, max_year, max_year)

# -------------------------
# Top 10 countries (only real countries)
# -------------------------
st.subheader("Top 10 countries (selected year)")

year_df = df[df["year"] == year].copy()

# ✅ keep ONLY real countries (ISO-3 codes like DEU, USA, CHN)
year_df = year_df[
    year_df["iso_code"].notna() &
    (year_df["iso_code"].astype(str).str.len() == 3)
]

year_df = year_df.dropna(subset=["co2"])

top10 = year_df.sort_values("co2", ascending=False).head(10)

fig, ax = plt.subplots()
ax.barh(top10["country"], top10["co2"])
ax.invert_yaxis()
ax.set_xlabel("CO₂ emissions (million tonnes per year)")
st.pyplot(fig)

# -------------------------
# World trend
# -------------------------
st.subheader("World CO₂ over time")

world = df[df["country"] == "World"].copy()
world = world.dropna(subset=["co2"])

fig, ax = plt.subplots()
ax.plot(world["year"], world["co2"])
ax.set_xlabel("Year")
ax.set_ylabel("CO₂ emissions (million tonnes per year)")
st.pyplot(fig)
