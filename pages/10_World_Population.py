import streamlit as st
import pandas as pd
import io

st.title("World Population")
st.write(
    """
Analysing world population data
"""
)

population_data = pd.read_csv("data/population.csv")

st.header("Data Summary")
st.write(population_data.head())

st.header("Select data by Country")
selected_country = st.selectbox("Country", sorted(population_data["Country (or dependency)"]))
filtered_df = population_data[population_data['Country (or dependency)'] == selected_country]
st.write(filtered_df)

# Cleaning Dataset
population_data["Migrants (net)"].fillna(population_data["Migrants (net)"].median(), inplace = True)
population_data["Yearly Change"] = population_data["Yearly Change"].str.replace(' %', '').astype(float)

st.header("Dataset Information")
st.write(population_data.describe())