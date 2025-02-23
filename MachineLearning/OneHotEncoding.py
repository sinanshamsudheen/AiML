import pandas as pd
import numpy as np
from sklearn import linear_model

#Dummy Variables Method
df=pd.read_csv("homeToHot.csv")
print(df)
dum=pd.get_dummies(df.town)
merged=pd.concat([df,dum],axis="columns")
print(merged)

final=merged.drop(['town','west windsor'],axis=1)

reg=linear_model.LinearRegression()
X=final.drop('price',axis=1)
Y=final.price
reg.fit(X,Y)

print(reg.predict([[2800,0,1]]))
print(reg.score(X,Y))

#OneHotEncoding Method
from sklearn.preprocessing import LabelEncoder
le=LabelEncoder()

dfle=df
dfle.town=le.fit_transform(dfle.town)
print(dfle)

P=dfle[['town','area']].values
Q=dfle[['price']]
print("p here: ",P)

from sklearn.preprocessing import OneHotEncoder
ohe = OneHotEncoder(handle_unknown='ignore', sparse_output=False)
P_encoded = ohe.fit_transform(P[:, 0].reshape(-1, 1))
P_final = np.hstack((P_encoded[:, 1:], P[:, 1].reshape(-1, 1)))  # Keep area column

# Train model
model = linear_model.LinearRegression()
model.fit(P_final, Q)

# Predict
prediction = model.predict([[1, 0, 2800]])  # Make sure order matches
print(prediction)