#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 12:41:22 2021

@author: shivadhulipala
"""


from flask import Flask,request,render_template
import numpy as np
import pandas as pd
#from sklearn.preprocessing import MinMaxScaler
import joblib

# initialise flask
app = Flask(__name__,template_folder='Template')
#load model
model = joblib.load('nestoria1.pkl')
# launch home page
@app.route('/',methods = ['GET'])
def home():
    print("hello")
    # load html page
    return render_template('houses.html')

@app.route('/',methods = ['POST'])
def prediction():
    x_col=['Name','n_Bedrooms','Location', 'Area', 'PRICE_PER_SQFT']
    # info from user input
    d =[[x for x in request.form.values()]]
    data = pd.DataFrame(d,columns=x_col)
    dataset=data[['n_Bedrooms', 'Area', 'PRICE_PER_SQFT']]
    print(dataset)
    dataset = dataset.apply(pd.to_numeric)
    inp = np.sqrt(dataset)

    predict = model.predict(inp)[0][0]
    predict= round(predict,2)
    #print(predict)
    if predict<0:
        predict = -predict
        text = ("Price Predicted for the House is : ₹"+str(predict))
    else:
        text = ("Price Predicted for the House is : ₹"+str(predict))
    print(text)
    return render_template('houses.html',prediction_text = text)

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=8000)
    
    











