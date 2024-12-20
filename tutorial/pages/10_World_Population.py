import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.title("World Population")
st.write(
    """
Analysing world population data
"""
)

population_data = pd.read_csv("tutorial/data/population.csv")

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

# Plotting Data
st.header("Analyze Data")
# Get a list of unique countries
country_options = population_data['Country (or dependency)'].unique()

# Create a multiselect widget
selected_countries = st.multiselect('Select Countries', country_options)
filtered_data = population_data[population_data['Country (or dependency)'].isin(selected_countries)]

st.header("Population World Share")
# Create a scatter plot
fig, ax = plt.subplots()
sns.scatterplot(x="Population (2020)", y="World Share", data=filtered_data, ax=ax)
# Annotate each point with the country name
for i, row in filtered_data.iterrows():
    ax.annotate(row['Country (or dependency)'], (row['Population (2020)'], row['World Share']))
ax.set_title("Population vs. World Share")
ax.set_xlabel("Population (2020)")
ax.set_ylabel("World Share")
st.pyplot(fig)

st.header("Population vs. Median Age")
fig, ax = plt.subplots()
sns.scatterplot(x="Population (2020)", y="Med. Age", data=filtered_data, ax=ax)
for i, row in filtered_data.iterrows():
    ax.annotate(row['Country (or dependency)'], (row['Population (2020)'], row['Med. Age']))
ax.set_title("Population vs. Median Age")
ax.set_xlabel("Population (2020)")
ax.set_ylabel("Median Age")
st.pyplot(fig)

st.header("Fert. Rate vs. Median Age")
fig, ax = plt.subplots()
sns.scatterplot(x="Fert. Rate", y="Med. Age", data=filtered_data, ax=ax)
for i, row in filtered_data.iterrows():
    ax.annotate(row['Country (or dependency)'], (row['Fert. Rate'], row['Med. Age']))
ax.set_title("Fert. Rate vs. Median Age")
ax.set_xlabel("Fert. Rate")
ax.set_ylabel("Median Age")
st.pyplot(fig)

st.header("Net Change World Share")
fig, ax = plt.subplots()
sns.scatterplot(x="World Share", y="Net Change", data=filtered_data, ax=ax)
for i, row in filtered_data.iterrows():
    ax.annotate(row['Country (or dependency)'], (row['World Share'], row['Net Change']))
ax.set_title("Net Change World Share")
ax.set_xlabel("World Share")
ax.set_ylabel("Net Change")
st.pyplot(fig)