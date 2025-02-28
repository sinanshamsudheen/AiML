import pandas as pd
from sklearn.datasets import load_iris

iris=load_iris()
print(dir(iris))
df=pd.DataFrame(iris.data,columns=iris.feature_names)
df['target']=iris.target
df['flower_name']=df.target.apply(lambda x: iris.target_names[x])
print(df)

df0=df[df['target']==0]
df1=df[df['target']==1]
df2=df[df['target']==2]

import matplotlib.pyplot as plt

plt.xlabel("sepal length")
plt.ylabel("sepal width")
plt.scatter(df0['sepal length (cm)'],df0['sepal width (cm)'],color="red",marker='+')
plt.scatter(df1['sepal length (cm)'],df1['sepal width (cm)'],color="green",marker='.')
plt.show()


plt.xlabel("petal length")
plt.ylabel("petal width")
plt.scatter(df0['petal length (cm)'],df0['petal width (cm)'],color="red",marker='+')
plt.scatter(df1['petal length (cm)'],df1['petal width (cm)'],color="green",marker='.')
plt.show()

from sklearn.model_selection import train_test_split
X=df.drop(['target','flower_name'],axis=1)
Y=df.target

X_train, X_test, Y_train, Y_test=train_test_split(X,Y,test_size=0.2)

from sklearn.svm import SVC
model=SVC(C=10,kernel='linear',gamma=50)
model.fit(X_train,Y_train)
print(model.score(X_test,Y_test))