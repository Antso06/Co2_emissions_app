import streamlit as st
import matplotlib.pyplot as plt

st.title("Country Comparison🌍")

df = st.session_state.data.copy()

min_year = int(df["year"].min())
max_year = int(df["year"].max())

year_range = st.slider("Year range", min_year, max_year, (1990, max_year))

metric = st.selectbox("Metric", ["co2", "co2_per_capita"])

countries = sorted(df["country"].dropna().unique())
selected = st.multiselect("Countries", countries,)

data = df[
    (df["year"] >= year_range[0]) &
    (df["year"] <= year_range[1]) &
    (df["country"].isin(selected))
].copy()

if len(selected) == 0:
    st.write("Please select at least one country.")
else:
    fig, ax = plt.subplots()
    for c in selected:
        temp = data[data["country"] == c].dropna(subset=[metric])
        ax.plot(temp["year"], temp[metric], label=c)

    ax.set_xlabel("Year")
    ax.set_ylabel(metric)
    ax.legend()
    st.pyplot(fig)
