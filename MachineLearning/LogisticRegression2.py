import pandas as pd
from sklearn.datasets import load_digits
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.metrics import confusion_matrix

digits=load_digits()
print(digits.data[0])
plt.gray()
# plt.matshow(digits.images[0])

X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.2)

from sklearn.linear_model import LogisticRegression

model=LogisticRegression()
model.fit(X_train,y_train)

print(model.score(X_test,y_test))

plt.matshow(digits.images[67])
print("Prediction: ",model.predict([digits.data[67]]))
print("Target: ",digits.target[67])


y_predicted=model.predict(X_test)
cm=confusion_matrix(y_test,y_predicted)
print(cm)

import seaborn as sns

plt.figure(figsize=(10,7))
sns.heatmap(cm,annot=True)
plt.xlabel('Predicted')
plt.ylabel('Truth')

plt.show()