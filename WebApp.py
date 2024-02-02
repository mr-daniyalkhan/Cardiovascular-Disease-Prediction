#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec  7 23:01:42 2023

@author: mac
"""


import numpy as np
import pickle
from pathlib import Path
import streamlit as st
import streamlit_authenticator as stauth





names = ["Muhammad Kashir Khan","Muhammad Daniyal Khan"]

usernames = ["mkashirk", "mdaniyalk"]

file_path = Path(__file__).parent / "LOGIN.pkl"
with file_path.open("rb") as file:
    hashed_passwords = pickle.load(file)
    
    
authenticator = stauth.Authenticate(names, usernames, hashed_passwords, "cvd_prediction", "abcdef", cookie_expiry_days=30)    


name, authentication_status, username = authenticator.login("Login", "main")


if authentication_status == False:
    st.error("Username or Password is incorrect")
    
if authentication_status == None:
    st.warning("Please Enter Username and Password")
    
if authentication_status:
    
    authenticator.logout("Logout", "main")
    
    st.sidebar.title(f"Welcome!\n {name}")
    st.sidebar.image("/Users/mac/Documents/D/Documents/University/Final Model/doctor.png",
             caption="I'll help you diagnose your heart health! - Dr. Random Forest Classifier",
             width=200)
    
    
    

    loaded_model = pickle.load(open('/Users/mac/Documents/D/Documents/University/Final Model/RandomForestModel.sav','rb'))
    
    def cvd_prediction(input_data):
        
    
        input_data_as_numpy_array = np.asarray(input_data)
    
        input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)
    
        Prediction = loaded_model.predict(input_data_reshaped)
        
        prediction_prob = loaded_model.predict_proba(input_data_reshaped)
    
        print(Prediction)
        
        if (Prediction[0]==0):
            st.markdown(f"**The probability that you'll have"
                        f" heart disease is {round(prediction_prob[0][1] * 100, 2)}%."
                        f" You are healthy!**")
            st.image("/Users/mac/Documents/D/Documents/University/Final Model/heart-okay.jpg",
                     caption="Your heart seems to be okay! - Dr. Random Forest Classifier")
            
        
            
        else:
            st.markdown(f"**The probability that you will have"
                   f" heart disease is {round(prediction_prob[0][1] * 100, 2)}%."
                   f" It sounds like you are not healthy.**")
            st.image("/Users/mac/Documents/D/Documents/University/Final Model/heart-bad.jpg",
                    caption="I'm not satisfied with the condition of your heart! - Dr. Random Forest Classifier")
            
        
        
    
    def main():
        
        col1, col2 = st.columns([2,1]) 


        col1.title('CardioPredict')


        image_path = "/Users/mac/Documents/D/Documents/University/Final Model/heart-sidebar.png"
        col2.image(image_path, width=115, caption="")
       
        
        
        BMI = st.text_input('ENTER YOUR BODY MASS INDEX ')
        
        Smoking = st.selectbox("DO YOU SMOKE ? \n\r[Yes = 1, " "  No = 0]", options=("0","1"))
        
        AlcoholDrinking = st.selectbox("DO YOU DRINK ALCOHOL ? \n\r[Yes = 1, " "  No = 0]", options=("0","1"))
        
        Stroke = st.selectbox("HAVE YOU EVER HAD A STROKE ? \n\r[Yes = 1, " "  No = 0]", options=("0","1"))
        
        PhysicalHealth = st.text_input('Physical Health Levels')
        
        Sex = st.selectbox("GENDER:\n\r[Female = 1, " " Male = 0]", options=("1","0"))
        
        AgeCategory = st.selectbox("WHAT IS YOUR AGE CATEGORY ?:\n\r[18-24 = 0, " " 25-29 = 1, " " 30-34 = 2, " " 35-39 = 3, " " 40-44 = 4, " " 45-49 = 5, "" 50-54 = 6, " " \n\r55-59 = 7, " " 60-64 = 8, " " 65-69 = 9, " "  70-74 = 10, " " 75-79 = 11, " " 80 or Older = 12]", options=("0","1","2","3","4","5","6","7","8","9","10","11","12"))
        
        Diabetic = st.selectbox("GLUCOSE LEVEL ? \n\r[Normal = 0, " " Borderline = 1, " "  High = 2, " " Excessive = 3]", options=("0","1","2","3"))
        
        PhysicalActivity = st.selectbox("ARE YOU PHYSICALLY ACTIVE ? \n\r[Yes = 1, " "  No = 0]", options=("0","1"))
        
        GenHealth = st.selectbox("GENERAL HEALTH\n\r[Poor = 0, Fair = 1, Good = 2, Very Good = 3, Excellent = 4  ]", options=("0","1","2","3","4"))
        
        SleepTime = st.text_input('Enter Your Sleep Time')
        
        Asthma = st.selectbox("DO YOU HAVE ASTHMA ? \n\r[Yes = 1, " "  No = 0]", options=("0","1"))
        
        
        
        
        diagnosis = ''
        
        
        
        if st.button('Predict Risk of Disease'):
            diagnosis = cvd_prediction([BMI,Smoking,AlcoholDrinking,Stroke,PhysicalHealth,Sex,AgeCategory,Diabetic,PhysicalActivity,GenHealth,SleepTime,Asthma])
            
    
        st.success(diagnosis)
        
        
        
    if  __name__ == '__main__':
        main()