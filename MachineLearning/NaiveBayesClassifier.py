import pandas as pd

df = pd.read_csv("titanic.csv", encoding='utf-8')
print(df)
inputs=df.drop(['PassengerId','Name','SibSp','Parch','Cabin','Embarked','Survived','Ticket'],axis=1)
target=df.Survived 

dummies=pd.get_dummies(df.Sex)
inputs=pd.concat([inputs,dummies],axis=1)
inputs.drop(['Sex'],axis=1,inplace=True)
inputs['Age'].fillna(inputs['Age'].mean(),inplace=True)
print(inputs.isna().any())

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test=train_test_split(inputs,target,test_size=0.2)

from sklearn.naive_bayes import GaussianNB
model=GaussianNB()
model.fit(X_train,Y_train)

print(model.score(X_test,Y_test))
print(model.predict_proba(X_test[:10]))