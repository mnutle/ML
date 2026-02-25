# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 10:05:31 2026
@author: Lab
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

# load model
loan_model = pickle.load(open("loan_model.sav",'rb'))
ridingmower_model = pickle.load(open("RidingMowers_model.sav",'rb'))
stress_model = pickle.load(open("stress_model.sav",'rb'))

# Sidebar menu
with st.sidebar:
    selected = option_menu('Classification',
                           ['LOAN','RidingMower','Stress'])

# ================= LOAN =================
if selected == 'LOAN':
    st.title('Loan Prediction')

    Income = st.text_input('Income')
    LoanAmount = st.text_input('Loan Amount')

    loan_predict = ''

    if st.button('Predict'):
        loan_predict = loan_model.predict([[float(Income),
                                            float(LoanAmount)]])
        st.success(loan_predict)

# ================= RidingMower =================
elif selected == 'RidingMower':
    st.title('RidingMower Prediction')

    Income = st.text_input('Income')
    lotsize = st.text_input('Lot Size')

    RidingMower_predict = ''

    if st.button('Predict'):
        RidingMower_predict = ridingmower_model.predict([[float(Income),
                                                          float(lotsize)]])
        if RidingMower_predict[0] == 0:
            RidingMower_predict = 'Non Owner'
        else:
            RidingMower_predict = 'Owner'

        st.success(RidingMower_predict)

# ================= Stress =================
elif selected == 'Stress':
    st.title('Stress Prediction')

    Age = st.text_input('Age')
    Gender = st.text_input('Gender')
    Occupation = st.text_input('Occupation')
    Device_Type = st.text_input('Device Type')
    Daily_Phone_Hours = st.text_input('Daily Phone Hours')
    Social_Media_Hours = st.text_input('Social Media Hours')
    Work_Productivity_Score = st.text_input('Work Productivity Score')
    Sleep_Hours = st.text_input('Sleep Hours')
    App_Usage_Count = st.text_input('App Usage Count')
    Caffeine_Intake_Cups = st.text_input('Caffeine Intake Cups')
    Weekend_Screen_Time_Hours = st.text_input('Weekend Screen Time Hours')

    stress_predict = ''

    if st.button('Predict'):
        stress_predict = stress_model.predict([[float(Age),
                                                float(Gender),
                                                float(Occupation),
                                                float(Device_Type),
                                                float(Daily_Phone_Hours),
                                                float(Social_Media_Hours),
                                                float(Work_Productivity_Score),
                                                float(Sleep_Hours),
                                                float(App_Usage_Count),
                                                float(Caffeine_Intake_Cups),
                                                float(Weekend_Screen_Time_Hours)]])
        st.success(stress_predict)