import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model

df=pd.read_csv("homeprices.csv")

model=linear_model.LinearRegression()
model.fit(df[['area']],df.price)
print(f"The model prediction: {model.predict([[3300]])}")

#Trying Pickle
import pickle
with open('Model_pickle','wb') as f:
    pickle.dump(model,f)

with open('Model_pickle','rb') as f:
    mp=pickle.load(f)
print(f"pickle model prediction: {mp.predict([[3300]])}")

#Trying joblib
import joblib
joblib.dump(model,'Model_joblib')
jb=joblib.load('Model_joblib')
print(f"joblib model prediction: {jb.predict([[3300]])}")