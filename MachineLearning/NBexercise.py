from sklearn.datasets import load_wine
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
import numpy as np
import pandas as pd
from sklearn.model_selection import train_test_split

wine=load_wine()
df=pd.DataFrame(wine.data, columns=wine.feature_names)
df['target']=wine.target
print(df)

X_train,X_test,Y_train,Y_test=train_test_split(wine.data,wine.target,test_size=0.3,random_state=100)
mb=MultinomialNB()
mb.fit(X_train,Y_train)
print("Multinomial score: ",mb.score(X_test,Y_test))

gb=GaussianNB()
gb.fit(X_train,Y_train)
print("Gaussian score: ",gb.score(X_test,Y_test))