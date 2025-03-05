import pandas as pd
import numpy as np
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.model_selection import cross_val_score
iris=load_iris()
X_train,X_test,Y_train,Y_test=train_test_split(iris.data,iris.target,test_size=0.2)

model=SVC()
model.fit(X_train,Y_train)
print(cross_val_score(model,X_test,Y_test))

########################
kernals=['linear','rbf']
C=[1,10,20]
avg_scores={}
for kvals in kernals:
    for cval in C:
        score=cross_val_score(SVC(kernel=kvals,C=cval,gamma='auto'),iris.data,iris.target,cv=5)
        avg_scores[kvals+'_'+str(cval)]=np.average(score)
##################### will be replaced by GridSearchCV
from sklearn.model_selection import GridSearchCV
gs=GridSearchCV(SVC(gamma='auto'),{
    'kernel':['linear','rbf'],
    'C':[1,10,20]
},cv=5,return_train_score=False)
gs.fit(iris.data,iris.target)
print(gs.cv_results_)

df=pd.DataFrame(gs.cv_results_)
print(df)
output=df[['param_C','param_kernel','mean_test_score']]
print(output)
print(gs.best_params_)

from sklearn.model_selection import RandomizedSearchCV
rs=RandomizedSearchCV(SVC(gamma='auto'),{
    'kernel':['linear','rbf'],
    'C':[1,10,20]
},cv=5,return_train_score=False,n_iter=2)
rs.fit(iris.data,iris.target)
df2=pd.DataFrame(rs.cv_results_)
df2=df2[['param_C','param_kernel','mean_test_score']]
print(df2)
####HOW TO CHOOSE THE BEST MODEL?####
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

model_params={
    'svm':{
        'model':SVC(gamma='auto'),
        'params':{
            'C':[1,10,20],
            'kernel':['linear','rbf']
        }
    },
    'random_forest':{
        'model':RandomForestClassifier(),
        'params':{
            'n_estimators':[1,5,10]
        }
    },
    'logistic_regression':{
        'model':LogisticRegression(solver='liblinear',multi_class='auto'),
        'params':{
            'C':[1,5,10]
        }
    }
}
scores=[]
for model_name,mp in model_params.items():
    mod=GridSearchCV(mp['model'],mp['params'],cv=5,return_train_score=False)
    mod.fit(iris.data,iris.target)
    scores.append({
        'model':model_name,
        'best_score':mod.best_score_,
        'best_params':mod.best_params_
    })

data=pd.DataFrame(scores,columns=['model','best_score','best_params'])
print(data)