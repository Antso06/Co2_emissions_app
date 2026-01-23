import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.title("Global Overview🌍")

df = st.session_state.data.copy()

min_year = int(df["year"].min())
max_year = int(df["year"].max())

year = st.slider("Year", min_year, max_year, max_year)

# 1) World trend (no fancy options)
st.subheader("World CO₂ over time")

world = df[df["country"] == "World"].copy()
world = world.dropna(subset=["co2"])

fig, ax = plt.subplots()
ax.plot(world["year"], world["co2"])
ax.set_xlabel("Year")
ax.set_ylabel("CO₂ (total)")
st.pyplot(fig)

# 2) Top 10 emitters for chosen year (fixed top 10)
st.subheader("Top 10 emitters (selected year)")

year_df = df[df["year"] == year].copy()
year_df = year_df.dropna(subset=["co2"])

top10 = year_df.sort_values("co2", ascending=False).head(10)

fig, ax = plt.subplots()
ax.barh(top10["country"], top10["co2"])
ax.invert_yaxis()
ax.set_xlabel("CO₂ (total)")
st.pyplot(fig)
