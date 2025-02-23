import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from word2number import w2n
import math

df=pd.read_csv("hiring.csv")
print(df)
print(w2n.word_to_num("Five"))
df.experience=df.experience.fillna("one")
median_score=math.floor(df['test_score(out of 10)'].median())
df['test_score(out of 10)']=df["test_score(out of 10)"].fillna(median_score)
df.experience = df.experience.apply(lambda x: w2n.word_to_num(x))
print(df)

reg=linear_model.LinearRegression()
reg.fit(df[['experience','test_score(out of 10)','interview_score(out of 10)']],df['salary($)'])

exp=int(input("enter experience: "))
test_sc=int(input("enter test_score(out of 10): "))
intw=int(input("enter interview_score(out of 10): "))
prediction=reg.predict([[exp,test_sc,intw]])

print(f"The expected salary is: {prediction}$")

# 2,9,6 = 51375$
#12,10,10 = 93523$
