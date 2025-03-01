import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.datasets import load_digits
import numpy as np
from sklearn.model_selection import train_test_split

digits=load_digits()
X_train, X_test, y_train, y_test = train_test_split(digits.data,digits.target,test_size=0.2)

#Test1
lr=LogisticRegression()
lr.fit(X_train,y_train)
print("LR score: ",lr.score(X_test,y_test))

# Test2
sv=SVC()
sv.fit(X_train,y_train)
print("SVM score: ",sv.score(X_test,y_test))

#Test3
fc=RandomForestClassifier(n_estimators=40)
fc.fit(X_train,y_train)
print("FC score: ",fc.score(X_test,y_test))

print("K FOLD,")
from sklearn.model_selection import KFold
kf=KFold(n_splits=3)

for train_index, test_index in kf.split([1,2,3,4,5,6,7,8,9]):
    print(train_index,test_index)

def get_score(model,X_train, X_test, y_train, y_test):
    model.fit(X_train,y_train)
    return model.score(X_test,y_test)

from sklearn.model_selection import StratifiedKFold
folds=StratifiedKFold(n_splits=3)

######
score_LR=[]
score_SVM=[]
score_RF=[]
for train_index, test_index in folds.split(digits.data, digits.target):
    X_train, X_test, y_train, y_test=digits.data[train_index],digits.data[test_index],digits.target[train_index],digits.target[test_index]
    score_LR.append(get_score(lr,X_train, X_test, y_train, y_test))
    score_SVM.append(get_score(sv,X_train, X_test, y_train, y_test))
    score_RF.append(get_score(fc,X_train, X_test, y_train, y_test))
####### The above set of code is replaced by the below module!!

from sklearn.model_selection import cross_val_score
print("lr scores: ",cross_val_score(lr,digits.data,digits.target))
print("SVM scores: ",cross_val_score(sv,digits.data,digits.target))
print("RF scores: ",cross_val_score(fc,digits.data,digits.target))

print("lr scores avg: ",cross_val_score(lr,digits.data,digits.target).mean())
print("SVM scores avg: ",cross_val_score(sv,digits.data,digits.target).mean())
print("RF scores avg: ",cross_val_score(fc,digits.data,digits.target).mean())
