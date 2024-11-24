import streamlit as st
import pandas as pd
import numpy as np

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

population_data["Fert. Rate"] = population_data["Fert. Rate"].replace('N.A.', np.nan).astype(float)
population_data["Fert. Rate"].fillna(population_data["Fert. Rate"].median(), inplace = True)

population_data["Med. Age"] = population_data["Med. Age"].replace('N.A.', np.nan).astype(float)
population_data["Med. Age"].fillna(population_data["Med. Age"].median(), inplace = True)

population_data["Urban Pop %"] = population_data["Urban Pop %"].str.replace(' %', '').replace('N.A.', np.nan).astype(float)
population_data["Urban Pop %"].fillna(population_data["Urban Pop %"].median(), inplace = True)

population_data["World Share"] = population_data["World Share"].str.replace(' %', '').replace('N.A.', np.nan).astype(float)
population_data["World Share"].fillna(population_data["World Share"].median(), inplace = True)

if (population_data.duplicated().any()):
    population_data.drop_duplicates(inplace = True)

st.header("Dataset Information")
st.write(population_data.describe())

st.header("Find Correlations")
# Select only numeric columns
numeric_cols = population_data.select_dtypes(include=['number'])

# Calculate the correlation matrix and display
st.write(numeric_cols.corr())