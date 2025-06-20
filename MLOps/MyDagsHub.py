from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from xgboost import XGBClassifier
from sklearn.svm import SVC  # import SVM

models = [
    (
        "Logistic Regression", 
        {"C": 1, "solver": 'liblinear'},
        LogisticRegression(), 
        (X_train, y_train),
        (X_test, y_test)
    ),
    (
        "Random Forest", 
        {"n_estimators": 30, "max_depth": 3},
        RandomForestClassifier(), 
        (X_train, y_train),
        (X_test, y_test)
    ),
    (
        "XGBClassifier",
        {"use_label_encoder": False, "eval_metric": 'logloss'},
        XGBClassifier(), 
        (X_train, y_train),
        (X_test, y_test)
    ),
    (
        "SVM", 
        {"C": 1.0, "kernel": "rbf"},
        SVC(probability=True),        
        (X_train, y_train),
        (X_test, y_test)
    )
]



reports = []

for model_name, params, model, train_set, test_set in models:
    X_train = train_set[0]
    y_train = train_set[1]
    X_test = test_set[0]
    y_test = test_set[1]
    
    model.set_params(**params)
    model.fit(X_train, y_train)
    y_pred = model.predict(X_test)
    report = classification_report(y_test, y_pred, output_dict=True)
    reports.append(report)


import mlflow
import mlflow.sklearn
import mlflow.xgboost

# dagshub setup

import dagshub
dagshub.init(repo_owner='learnpythonlanguage', repo_name='mlflow_dagshub_demo', mlflow=True)


import os
os.environ['MLFLOW_TRACKING_USERNAME'] = 'sinanshamsudheen' # 'learnpythonlanguage'
os.environ['MLFLOW_TRACKING_PASSWORD'] = '' # 
os.environ['MLFLOW_TRACKING_URI'] = 'https://dagshub.com/sinanshamsudheen/TLflow.mlflow' # https://dagshub.com/learnpythonlanguage/mlflow_dagshub_demo.mlflow

# Initialize MLflow
mlflow.set_experiment( )
# mlflow.set_tracking_uri("http://localhost:5000")

for i, element in enumerate(models):
    model_name = element[0]
    params = element[1]
    model = element[2]
    report = reports[i]
    
    with mlflow.start_run(run_name=model_name):        
        mlflow.log_params(params)
        mlflow.log_metrics({
            'accuracy': report['accuracy'],
            'precision_class_1': report['1']['precision'],
            'precision_class_0': report['0']['precision'],
            'recall_class_1': report['1']['recall'],
            'recall_class_0': report['0']['recall'],
            'f1_score_macro': report['macro avg']['f1-score']
        })  
        
        if "XGB" in model_name:
            mlflow.xgboost.log_model(model, "model")
        else:
            mlflow.sklearn.log_model(model, "model")