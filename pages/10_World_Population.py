import streamlit as st
import pandas as pd

st.write("# World Population")

population_data = pd.read_csv("data/population.csv")
st.write(population_data)