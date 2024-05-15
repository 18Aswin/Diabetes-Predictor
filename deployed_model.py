# -*- coding: utf-8 -*-
"""
Created on Wed May 15 18:39:17 2024

@author: Aswin
"""

import numpy as np
import pickle

#Loading the saved model
diabetes_model = pickle.load(open('diabetes_predictor.sav', 'rb'))


input_data = (5, 166, 72, 19, 175, 25.8, 0.587, 51)

input_data_numpy = np.asarray(input_data)
input_data_reshape = input_data_numpy.reshape(1, -1)

prediction = diabetes_model.predict(input_data_reshape)
print(prediction)

if(prediction[0] == 1):
  print("The person is Diabetic")
else:
  print("The person is not Diabetic")