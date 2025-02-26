import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression

df=pd.read_csv("insurance_data.csv")
print(df)
plt.scatter(df.age,df.bought_insurance,marker='+',color="red")

x=df[['age']]
y=df.bought_insurance
X_train, X_test, Y_train, Y_test=train_test_split(x,y,test_size=0.1)
print(X_train)

model=LogisticRegression()
model.fit(X_train,Y_train)

print(model.predict(X_test))
print(Y_test)
print("Score: ",model.score(X_test,Y_test))
plt.plot(df['age'], model.predict(df[['age']]))
print(model.predict_proba(X_test))

plt.show()

