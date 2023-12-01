import pandas as pd
import numpy as np
from sklearn import datasets
import streamlit as st

from model.WineClassifierRandomForest import WineClassifierRandomForest

st.set_page_config(
    page_title="Sample of Wine Classification",
    page_icon="👋",
)

def load_model():
 model = WineClassifierRandomForest()
 return model

alcohol = st.number_input('Alcohol', min_value=11.0, max_value=14.8)
malic_acid = st.number_input('Malic Acid', min_value=0.74, max_value=5.80)
ash = st.number_input('Ash', min_value=1.36, max_value=3.23)
alcalinity_of_ash = st.number_input('Alcalinity of Ash', min_value=10.6, max_value=30.0)
magnesium = st.number_input('Magnesium', min_value=70.0, max_value=162.0)
total_phenols = st.number_input('Total Phenols', min_value=0.98, max_value=3.88)
flavanoids = st.number_input('Flavanoids', min_value=0.34, max_value=5.08)
nonflavanoid_phenols = st.number_input('Non-Flavanoids Phenols', min_value=0.13, max_value=0.66)
proanthocyanins = st.number_input('Proanthocyanins', min_value=0.41, max_value=3.58)
color_intensity = st.number_input('Colour Intensity', min_value=1.3, max_value=13.0)
hue = st.number_input('Hue', min_value=0.48, max_value=1.71)
diluted_wines = st.number_input('OD280/OD315 of diluted wines', min_value=1.27, max_value=4.00)
proline = st.number_input('Proline', min_value=278, max_value=1680)

predict_list = [
 alcohol,
 malic_acid,
 ash,
 alcalinity_of_ash,
 magnesium,
 total_phenols,
 flavanoids,
 nonflavanoid_phenols,
 proanthocyanins,
 color_intensity,
 hue,
 diluted_wines,
 proline
]


predict_list = [float(number) for number in predict_list]
predict_list = np.array(predict_list).reshape(1, 13)
wine_data = datasets.load_wine()
feature_names = wine_data['feature_names']
df = pd.DataFrame(predict_list, columns=feature_names)

if st.button("Predict"):
 model = load_model()

 prediction = model.predict(df)

 st.header("Model Prediction")
 st.dataframe(df)
 st.subheader(f'Wine Class predicted {prediction[0]}')
