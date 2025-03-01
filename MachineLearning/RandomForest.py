import pandas as pd
import matplotlib.pyplot as plt
from sklearn.datasets import load_digits

digits=load_digits()
print(dir(digits))
plt.gray()
# for i in range(4):
#     plt.matshow(digits.images[i]) 
df=pd.DataFrame(digits.data, columns=digits.feature_names)
df['target']=digits.target
print(df)
X=df.drop(['target'],axis=1)
y=df.target

from sklearn.model_selection import train_test_split

X_train, X_test, y_train, y_test = train_test_split(X,y,test_size=0.2)
from sklearn.ensemble import RandomForestClassifier #ensemble : to take in multiple algorithms (here its multiple decision trees)
model=RandomForestClassifier(n_estimators=50)
model.fit(X_train,y_train)
print("score: ",model.score(X_test,y_test))

from sklearn.metrics import confusion_matrix
y_predicted=model.predict(X_test)
cm=confusion_matrix(y_test,y_predicted)

import seaborn as sns
sns.heatmap(cm, annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

plt.show()