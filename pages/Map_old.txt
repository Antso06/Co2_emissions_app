import streamlit as st

st.title("Check my awesome map🗺️")

df = st.session_state.data.copy()

# For the map we need lat/long
df = df.loc[~df["latitude"].isna(), :]

# Keep it simple: map points for a single year
year = st.slider("Year", int(df["year"].min()), int(df["year"].max()), int(df["year"].max()))
df = df[df["year"] == year]

st.dataframe(df.head(50))
st.map(data=df, latitude="latitude", longitude="longitude")
