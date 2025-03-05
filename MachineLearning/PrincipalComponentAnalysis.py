import pandas as pd

from sklearn.datasets import load_digits

digits=load_digits()
print(digits.keys())

df=pd.DataFrame(digits.data,columns=digits.feature_names)
print(df)

X=df
Y=digits.target
from sklearn.preprocessing import MinMaxScaler
scaler=MinMaxScaler()
x_sc=scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(x_sc,Y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=1000)
model.fit(X_train,Y_train)
print(model.score(X_test,Y_test))

from sklearn.decomposition import PCA
pca=PCA(0.95)
x_pca=pca.fit_transform(X)

X_train_pca, X_test_pca, Y_train_pca, Y_test_pca = train_test_split(x_pca,Y,test_size=0.2)

from sklearn.linear_model import LogisticRegression
model=LogisticRegression(max_iter=1000)
model.fit(X_train_pca,Y_train_pca)
print(model.score(X_test_pca,Y_test_pca))