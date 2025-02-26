import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.preprocessing import LabelEncoder
import numpy as np

# Specify the full path if the file is in a different directory
df = pd.read_csv("titanic.csv", encoding='utf-8')
print(df)
inputs=df.drop(['PassengerId','Name','SibSp','Parch','Cabin','Embarked','Survived'],axis=1)
target=df.Survived
median_age=df['Age'].median()
inputs.Age=inputs.Age.fillna(median_age,inplace=True)

print(df.isna().any())

Pclass_le=LabelEncoder()
Sex_le=LabelEncoder()
Age_le=LabelEncoder()
Ticket_le=LabelEncoder()
Fare_le=LabelEncoder()

model=tree.DecisionTreeClassifier()
inputs['Pclass_n']=Pclass_le.fit_transform(df['Pclass'])
inputs['Sex_n']=Sex_le.fit_transform(df['Sex'])
inputs['Age_n']=Age_le.fit_transform(df['Age'])
inputs['Ticket_n']=Ticket_le.fit_transform(df['Ticket'])
inputs['Fare_n']=Fare_le.fit_transform(df['Fare'])

inputs_n=inputs.drop(['Pclass','Sex','Ticket','Fare','Age'],axis=1)
print(inputs)
print(inputs_n)

X_train, X_test, Y_train, Y_test = train_test_split(inputs_n,target,test_size=0.2)
model.fit(X_train,Y_train)

print("Score: ",model.score(X_test,Y_test))
print("Prediction: ",model.predict(X_test))

print("test: ",Y_test)
