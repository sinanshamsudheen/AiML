import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn import linear_model
import math
df=pd.read_csv("home.csv")
print(df)

median_bedrooms=math.floor(df.bedrooms.median())

df.bedrooms=df.bedrooms.fillna(median_bedrooms)

reg=linear_model.LinearRegression()
reg.fit(df[['area','bedrooms','age']],df.price)

print("coeff",reg.coef_)
print("intercept: ",reg.intercept_)

print(f"predicted price: {reg.predict([[4100,6,8]])}")
# y=m1*area + m2*bedrooms + m3*age + intercept
y= 4100*112.06244194 + 6*23388.88007794 - 8*3231.71790863 + 221323.0018654043
print("solution y:", y)