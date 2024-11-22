import streamlit as st
import pandas as pd

st.write("# Ayubowan!")
x = st.text_input("Type anything...")
st.write(f"You typed: {x}")

population_data = pd.read_csv("data/population.csv")
st.write(population_data)