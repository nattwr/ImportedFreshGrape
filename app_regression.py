import streamlit as st
import pandas as pd
import pickle

# Load the trained model
with open('pipeline_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Title of the app
st.title('Import Value Prediction App')

# Input fields for user to enter data
weight = st.number_input('Enter weight (น้ำหนัก สถิติ):')
volume = st.number_input('Enter volume (ปริมาณ สถิติ):')
unit = st.selectbox('Select unit (หน่วยปริมาณ):', ['BK','BX','CT','KGM','PK','CS','PA','C62','SET','BE','EA','PU','D97','TNE','CK','BG','CR'])  # Replace with actual units
country = st.selectbox('Select country (ประเทศถิ่นกำเนิด):', ['CN','IN','PE','AU','JP','US','ZA','CL','KR','CA','PL','UA','NZ','KE','TR'])  # Replace with actual units
#'statistic_weight', 'statistic_qty', 'qty_unit', 'country_of_origin'
# Create a DataFrame for the input
input_data = pd.DataFrame({
    'statistic_weight': [weight],
    'statistic_qty': [volume],
    'qty_unit': [unit],
    'country_of_origin': [country]
})

# Make prediction
if st.button('Predict'):
    prediction = model.predict(input_data)
    st.write(f'Predicted Import Value (มูลค่านำเข้าเงินบาท): {round(prediction[0],2)}')
