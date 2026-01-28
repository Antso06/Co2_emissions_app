import streamlit as st
import matplotlib.pyplot as plt

st.title("Country Comparison 🌍")

# make sure data exists (important in multipage apps)
if "data" not in st.session_state:
    st.error("Data not loaded. Please open the main page first.")
    st.stop()

df = st.session_state.data.copy()

min_year = int(df["year"].min())
max_year = int(df["year"].max())

year_range = st.slider("Year range", min_year, max_year, (1990, max_year))

metric = st.selectbox("Metric", ["co2", "co2_per_capita"])

countries = sorted(df["country"].dropna().unique())
selected = st.multiselect("Countries", countries)

data = df[
    (df["year"] >= year_range[0]) &
    (df["year"] <= year_range[1]) &
    (df["country"].isin(selected))
].copy()

if len(selected) == 0:
    st.info("Please select at least one country.")
else:
    fig, ax = plt.subplots()

    for c in selected:
        temp = data[data["country"] == c].dropna(subset=[metric])
        ax.plot(temp["year"], temp[metric], label=c)

    ax.set_xlabel("Year")

    if metric == "co2":
        ax.set_ylabel("CO₂ emissions (million tonnes per year)")
    else:
        ax.set_ylabel("CO₂ emissions (tonnes per person per year)")

    ax.set_title("CO₂ emissions by country over time")
    ax.legend()

    st.pyplot(fig)
