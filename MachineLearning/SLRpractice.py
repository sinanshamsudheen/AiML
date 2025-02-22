import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("canada_per_capita_income.csv")
print(df)

reg=linear_model.LinearRegression()
reg.fit(df[['year']],df['per capita income (US$)'])


plt.scatter(df['year'],df['per capita income (US$)'],marker='+',color="red")
plt.ylabel("per capita income (US$)")
plt.xlabel("year")
plt.plot(df['year'],reg.predict(df[['year']]),color="blue")
plt.show()
print(f"expected price during 2018: {reg.predict([[2020]])}")

p=reg.predict(df[['year']])
df['prices']=p
print(df)