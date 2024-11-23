import streamlit as st
import pandas as pd
import shap
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestRegressor

st.write("""
# California House Price Prediction App

This app predicts the **California House Price**!
""")
st.write('---')

# Loads the California House Price Dataset
from sklearn.datasets import fetch_california_housing  # For California housing

housing = fetch_california_housing(as_frame=True)
X = pd.DataFrame(housing.data)
Y = pd.DataFrame(housing.target)

# Sidebar
# Header of Specify Input Parameters
st.header('Specify Input Parameters')

st.write(X)

def user_input_features():
    # Using sliders for each feature in the California housing dataset
    MedInc = st.slider('MedInc', X.MedInc.min(), X.MedInc.max(), X.MedInc.mean())
    HouseAge = st.slider('HouseAge', X.HouseAge.min(), X.HouseAge.max(), X.HouseAge.mean())
    AveRooms = st.slider('AveRooms', X.AveRooms.min(), X.AveRooms.max(), X.AveRooms.mean())
    AveBedrms = st.slider('AveBedrms', X.AveBedrms.min(), X.AveBedrms.max(), X.AveBedrms.mean())
    Population = st.slider('Population', X.Population.min(), X.Population.max(), X.Population.mean())
    AveOccup = st.slider('AveOccup', X.AveOccup.min(), X.AveOccup.max(), X.AveOccup.mean())
    Latitude = st.slider('Latitude', X.Latitude.min(), X.Latitude.max(), X.Latitude.mean())
    Longitude = st.slider('Longitude', X.Longitude.min(), X.Longitude.max(), X.Longitude.mean())

    # Constructing the input data as a DataFrame
    data = {
        'MedInc': MedInc,
        'HouseAge': HouseAge,
        'AveRooms': AveRooms,
        'AveBedrms': AveBedrms,
        'Population': Population,
        'AveOccup': AveOccup,
        'Latitude': Latitude,
        'Longitude': Longitude
    }
    features = pd.DataFrame(data, index=[0])
    return features

df = user_input_features()

# Main Panel

# Print specified input parameters
st.header('Specified Input parameters')
st.write(df)
st.write('---')

if st.button('Train and Predict'):
    # Build Regression Model
    model = RandomForestRegressor()
    model.fit(X, Y.values.ravel())
    # Apply Model to Make Prediction
    prediction = model.predict(df)

    st.header('Prediction')
    st.write(prediction)
    st.write('---')

# Explaining the model's predictions using SHAP values
# https://github.com/slundberg/shap
def explain_model():
    explainer = shap.TreeExplainer(model)
    shap_values = explainer.shap_values(X)

    st.header('Feature Importance')
    plt.title('Feature importance based on SHAP values')
    shap.summary_plot(shap_values, X)
    st.pyplot(bbox_inches='tight')
    st.write('---')

    plt.title('Feature importance based on SHAP values (Bar)')
    shap.summary_plot(shap_values, X, plot_type="bar")
    st.pyplot(bbox_inches='tight')