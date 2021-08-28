import streamlit as st
import pandas as pd
import pickle
import numpy as np
from streamlit.state.session_state import Serialized


st.markdown(
    """
    <div>
        <center><h1>Medical Cost Predictor</h1></center>
    </div>
    """,
    unsafe_allow_html=True,
)
st.write("### Information of the beneficiary")
model = pickle.load(open("Model/model.pkl", "rb"))

input = []
# Age
input.append(st.slider("Enter his/her age", 0, 100))

# Sex
S = st.radio("Gender of beneficiary", ("Male", "Female"))
if S == "Male":
    S_result = 1
else:
    S_result = 0
input.append(S_result)

# BMI
input.append(st.text_input("Enter his/her BMI"))

# Children
input.append(st.selectbox("How many children does he/she have?", [0, 1, 2, 3, 4, 5]))

# Smoke
D = st.radio("Does he/she smoke?", ("Yes", "No"))
if D == "Yes":
    D_result = 1
else:
    D_result = 0
input.append(D_result)

# Region
R = st.selectbox(
    "Select the region", ("Northeast", "Northwest", "Southeast", "Southwest")
)
if R == "Northeast":
    R_res = 0
elif R == "Northwest":
    R_res = 1
elif R == "Southeast":
    R_res = 2
elif R == "Southwest":
    R_res = 3
input.append(R_res)

# Prediction
try:
    if st.button("Predict"):
        p = model.predict([input])
        st.success(f"The estimated medical cost is ${round(float(p),2)}")
except:
    st.error("Please try again")