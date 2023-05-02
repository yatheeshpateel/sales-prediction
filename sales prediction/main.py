import streamlit as st
import joblib
import warnings
from sklearn.exceptions import ConvergenceWarning

with warnings.catch_warnings():
    warnings.filterwarnings("ignore", category=ConvergenceWarning)
    model = joblib.load('model_joblib_test')


model = joblib.load('model_joblib_test')

st.title("SalesPrediction")

slno = st.number_input("slno")
tv = st.number_input("TV")
radio= st.number_input("Radio")
newspaper= st.number_input("Newspaper")



if st.button("Predict"):
   
   
    result = model.predict([[slno,tv,radio,newspaper]])
    st.write("Sales:" , result[0])

  