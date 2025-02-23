import pandas as pd
import numpy as np
from sklearn import linear_model

df=pd.read_csv("carprices.csv")
print(df)
dum=pd.get_dummies(df['Car Model'])
merged=pd.concat([df,dum],axis=1)

merged=merged.drop(['Car Model','Mercedez Benz C class'],axis=1)

x=merged.drop('Sell Price($)',axis=1)
y=merged['Sell Price($)']
model=linear_model.LinearRegression()
model.fit(x,y)
print(x)
print(f"The Expected price of a 4yrs old mercedez benz with 450000 mileage is: {model.predict([[45000,4,0,0]])}")
print(f"The Expected price of a 7yrs old BMW X5 with 86000 mileage is: {model.predict([[86000,7,0,1]])}")
print(f"The score of my model is: {model.score(x,y)}")

# The Expected price of a 4yrs old mercedez benz with 450000 mileage is: [36991.31721061]
# The Expected price of a 7yrs old BMW X5 with 86000 mileage is: [11080.74313219]
# The score of my model is: 0.9417050937281082