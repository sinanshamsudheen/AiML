import pandas as pd

df=pd.read_csv("diabetes.csv")
print(df.isnull().sum())

X=df.drop('Outcome',axis=1)
Y=df.Outcome

from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_sc=scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(x_sc,Y,test_size=0.2,stratify=Y,random_state=10)

from sklearn.tree import DecisionTreeClassifier
# model=DecisionTreeClassifier()

from sklearn.model_selection import cross_val_score
scores=cross_val_score(DecisionTreeClassifier(),X_train,Y_train,cv=5)
print(scores.mean())

from sklearn.ensemble import BaggingClassifier
bag_model=BaggingClassifier(
    estimator=DecisionTreeClassifier(),
    n_estimators=100,
    random_state=0,
    oob_score=True,
    max_samples=0.8
)
bag_model.fit(X_train,Y_train)
print(bag_model.oob_score_)
print(bag_model.score(X_test,Y_test))

scores2=cross_val_score(bag_model,X,Y,cv=5)
print(scores2)