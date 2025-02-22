import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("homeprices.csv")

reg=linear_model.LinearRegression()
reg.fit(df[['area']],df.price)
print(f"The model prediction: {reg.predict([[3300]])}")

print(f"slope: {reg.coef_}") #slope
print(f"c value: {reg.intercept_}") # c or b value

y=reg.coef_*3300+reg.intercept_ #y=mx+c
print(y)

d=pd.read_csv("areas.csv")
p=reg.predict(d)
d['prices']=p
print(d)
d.to_csv("prediction.csv",index=False)

plt.xlabel("area(Square ft)")
plt.ylabel("price(USD)")
plt.scatter(df["area"],df["price"],marker='+',color="red")
plt.plot(df.area,reg.predict(df[['area']]),color="blue")
plt.show()