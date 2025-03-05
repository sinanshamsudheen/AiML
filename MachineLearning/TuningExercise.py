from sklearn.datasets import load_digits
from sklearn.linear_model import LogisticRegression
from sklearn.naive_bayes import GaussianNB
from sklearn.naive_bayes import MultinomialNB
from sklearn.tree import DecisionTreeClassifier
from sklearn.svm import SVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import GridSearchCV
import pandas as pd
digits=load_digits()

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
    },
    'gaussianNB':{
        'model':GaussianNB(),
        'params':{
            'var_smoothing':[1e-9, 1e-8, 1e-7, 1e-6, 1e-5]
        }
    },
    'multinomialNB':{
        'model':MultinomialNB(),
        'params':{
            'fit_prior':[True,False],
            'alpha':[0.0,0.1,0.5,1.0,5.0]
        }
    },
    'decision_tree':{
        'model':DecisionTreeClassifier(),
        'params':{
            'max_depth':[None,5,10,20],
            'min_samples_split':[2,5,10],
            'criterion':['gini','entropy']
        }
    }
}
scores=[]
for model_name,mp in model_params.items():
    clf=GridSearchCV(mp['model'],mp['params'],cv=5,return_train_score=False)
    clf.fit(digits.data,digits.target)
    scores.append({
        'model':model_name,
        'best_score':clf.best_score_,
        'best_params':clf.best_params_
    })
df=pd.DataFrame(scores,columns=['model','best_score','best_params'])
print(df)