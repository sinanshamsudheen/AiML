import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

def train_test(year):
    df=pd.read_csv("D:\VsCode\AiML\MachineLearning\canada_per_capita_income.csv")

    reg=linear_model.LinearRegression()
    reg.fit(df[['year']],df['per capita income (US$)'])

    p=reg.predict([[year]])
    return p

from fastapi import FastAPI
app=FastAPI()
@app.get("/Model/{value}")
async def Model(value: int):
    return f"Canada's Per capita income for the year {value} is: {float(train_test(value)[0]):.2f} (US$)"
