# -*- coding: utf-8 -*-
"""
Created on Wed Feb 18 10:05:31 2026

@author: Lab
"""

import pickle
import streamlit as st
from streamlit_option_menu import option_menu

#import model
loan_model = pickle.load(open("loan_model.sav",'rb'))
ridingmower_model = pickle.load(open("RidingMowers_model.sav",'rb'))
stress_model = pickle.load(open("stress_model.sav",'rb'))


with st.sidebar:
  
  selected = option_menu('Classification',['LOAN','RidingMower','Stress']) 

  if(selected == 'LOAN'):
    st.title('RidingMower Prediction')
    
    #user input
    Income = st.text_input('Income')
    lotsize = st.text_input('lotsize')
    
      
    RidingMower_predict = ''
      
    if st.button('Predict'):
      RidingMower_predict = ridingmower_model.predict([[
      float(Income),
      float(lotsize)
      ]])
          
      if(RidingMower_predict[0]==0):
        RidingMower_predict = 'Non Owner'
      else:
        RidingMower_predict = 'Owner'
    st.success(RidingMower_predict)

  if(selected == 'RidingMower'):
    st.title('RidingMower Prediction')
      
      #user input
    Income = st.text_input('Income')
    lotsize = st.text_input('lotsize')
    
      
    RidingMower_predict = ''
      
    if st.button('Predict'):
        RidingMower_predict = ridingmower_model.predict([[
            float(Income),
          float(lotsize)
          ]])
          
        if(RidingMower_predict[0]==0):
          RidingMower_predict = 'Non Owner'
        else:
          RidingMower_predict = 'Owner'
    st.success(RidingMower_predict)


  if(selected == 'Stress'):
    st.title('Stress Prediction')
      
      #user input
    Age = st.text_input('Age')
    Gender = st.text_input('Gender')
    Occupation = st.text_input('Occupation')
    Device_Type = st.text_input('Device_Type')
    Daily_Phone_Hours = st.text_input('Daily_Phone_Hours')
    Social_Media_Hours = st.text_input('Social_Media_Hours')
    Work_Productivity_Score = st.text_input('Work_Productivity_Score')
    Sleep_Hours = st.text_input('Sleep_Hours')
    App_Usage_Count = st.text_input('App_Usage_Count')
    Caffeine_Intake_Cups = st.text_input('Caffeine_Intake_Cups')
    Weekend_Screen_Time_Hours = st.text_input('Weekend_Screen_Time_Hours')
    
      
    stress_predict = ''
      
    if st.button('Predict'):
      stress_predict = stress_model.predict([[
              float(Age),
              float(Gender),
              float(Occupation),
              float(Device_Type),
              float(Daily_Phone_Hours),
              float(Social_Media_Hours),
              float(Work_Productivity_Score),
              float(Sleep_Hours),
              float(App_Usage_Count),
              float(Caffeine_Intake_Cups),
              float(Weekend_Screen_Time_Hours)
          ]])
          
          
    st.success(stress_predict)

   


