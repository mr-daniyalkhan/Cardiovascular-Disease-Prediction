#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Dec  8 00:07:16 2023

@author: mac
"""

import numpy as np
import pickle


loaded_model = pickle.load(open('/Users/mac/Documents/D/Documents/University/Final Model/RandomForestModel.sav','rb'))


input_data = (35,1,1,1,3,1,9,2,0,4,13,1)

input_data_as_numpy_array = np.asarray(input_data)

input_data_reshaped = input_data_as_numpy_array.reshape(1,-1)

Prediction = loaded_model.predict(input_data_reshaped)

prediction_prob = loaded_model.predict_proba(input_data_reshaped)

print(Prediction)

if (Prediction[0]==0):
    print(f"**The probability that you'll have"
                        f" heart disease is {round(prediction_prob[0][1] * 100, 2)}%."
                        f" You are healthy!**")
else:
    print(f"**The probability that you will have"
                        f" heart disease is {round(prediction_prob[0][1] * 100, 2)}%."
                        f" It sounds like you are not healthy.**")
        
    
    
    
    
    
    
    
    #print('The person does not have Heart Disease')
#else:
    #print ('The person has Heart Disease')