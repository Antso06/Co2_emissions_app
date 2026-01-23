import streamlit as st
import pandas as pd

st.set_page_config(page_title="CO2 App", page_icon="🌍")

st.title("CO₂ Emissions App🌍")

# Real datasets (loaded once here)
CO2_URL = "https://raw.githubusercontent.com/owid/co2-data/master/owid-co2-data.csv"
COUNTRIES_URL = "https://raw.githubusercontent.com/google/dspl/master/samples/google/canonical/countries.csv"

@st.cache_data
def load_data():
    co2 = pd.read_csv(CO2_URL)
    countries = pd.read_csv(COUNTRIES_URL)

    # Keep it simple: only columns we actually use
    co2 = co2[["country", "year", "co2", "co2_per_capita"]].copy()

    # Countries file has: country (2-letter), latitude, longitude, name
    countries = countries[["name", "latitude", "longitude"]].copy()

    # Merge by country name (not perfect, but simple for class)
    df = co2.merge(countries, left_on="country", right_on="name", how="left")
    df = df.drop(columns=["name"])

    return df

st.session_state.data = load_data()

st.write("Use the pages on the left to explore the data.")
st.dataframe(st.session_state.data.head(30))
