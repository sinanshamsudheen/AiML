import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn.model_selection import train_test_split
df=pd.read_csv("bmwprices.csv")
# print(df)

p=plt.scatter(df['Mileage'],df['Sell Price($)'])
q=plt.scatter(df['Age(yrs)'],df['Sell Price($)'])
# plt.show()

x=df[['Mileage','Age(yrs)']]
y=df['Sell Price($)']

X_train, X_test, Y_train, Y_test = train_test_split(x,y,test_size=0.2,random_state=10)
reg=linear_model.LinearRegression()
reg.fit(X_train,Y_train)

print("prediction: ",reg.predict(X_test))
print(Y_test)

print("Accuracy: ",reg.score(X_test,Y_test))