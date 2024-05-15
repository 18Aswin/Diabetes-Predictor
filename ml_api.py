# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import json

app = FastAPI()

class model_input(BaseModel):

    Pregnancies : int
    Glucose : int
    BloodPressure : int
    SkinThickness : int
    Insulin : int
    BMI : float
    DiabetesPedigreeFunction : float
    Age : int

#Loading the saved model

diabetes_model = pickle.load(open('diabetes_predictor.sav', 'rb'))

@app.post('/diabetes_prediction')
def diabetes_pred(input_parameters : model_input):

    input_data = input_parameters.json()
    input_dictionary = json.loads(input_data)

    preg = input_dictionary['Pregnancies']
    glu = input_dictionary['Glucose']
    bp = input_dictionary['BloodPressure']
    skin_thic = input_dictionary['SkinThickness']
    insulin = input_dictionary['Insulin']
    bmi = input_dictionary['BMI']
    dpf = input_dictionary['DiabetesPedigreeFunction']
    age = input_dictionary['Age']

    input_list = [preg, glu, bp, skin_thic, insulin, bmi, dpf, age]

    prediction = diabetes_model.predict([input_list])

    if prediction[0] == 0:
        return 'Person is not Diabetic'
    else:
        return 'Person is Diabetic'