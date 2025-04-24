# ------------------------------
# Preprocessing Templates (Optional)
# ------------------------------

# --- Use this for TEXT DATA ---
# from sklearn.feature_extraction.text import TfidfVectorizer
# vectorizer = TfidfVectorizer()
# X_train_vec = vectorizer.fit_transform(X_train)
# X_test_vec = vectorizer.transform(X_test)

# --- Use this for NUMERIC DATA ---
# from sklearn.preprocessing import StandardScaler
# scaler = StandardScaler()
# X_train_scaled = scaler.fit_transform(X_train)
# X_test_scaled = scaler.transform(X_test)

# You will provide X_train and y_train directly.

# ------------------------------
# Model Evaluation Function
# ------------------------------

def evaluate_models(X_train, y_train):
    if hasattr(X_train, "toarray"):
        X_train = X_train.toarray()

    from sklearn.svm import SVC
    from sklearn.ensemble import RandomForestClassifier, GradientBoostingClassifier, AdaBoostClassifier
    from sklearn.linear_model import LogisticRegression, RidgeClassifier, SGDClassifier
    from sklearn.naive_bayes import GaussianNB, MultinomialNB, BernoulliNB
    from sklearn.tree import DecisionTreeClassifier
    from sklearn.neighbors import KNeighborsClassifier
    from sklearn.neural_network import MLPClassifier
    from sklearn.model_selection import RandomizedSearchCV
    from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
    import pandas as pd
    import numpy as np

    model_params = {
        'svm': {
            'model': SVC(),
            'params': {
                'C': [0.1, 1, 10],
                'kernel': ['linear', 'rbf', 'poly'],
                'gamma': ['scale', 'auto']
            }
        },
        'random_forest': {
            'model': RandomForestClassifier(),
            'params': {
                'n_estimators': [50, 100, 200],
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5],
                'criterion': ['gini', 'entropy']
            }
        },
        'logistic_regression': {
            'model': LogisticRegression(solver='liblinear'),
            'params': {
                'C': [0.1, 1, 10],
                'penalty': ['l1', 'l2']
            }
        },
        'gaussianNB': {
            'model': GaussianNB(),
            'params': {
                'var_smoothing': [1e-9, 1e-8, 1e-7]
            }
        },
        'multinomialNB': {
            'model': MultinomialNB(),
            'params': {
                'alpha': [0.0, 0.1, 0.5, 1.0],
                'fit_prior': [True, False]
            }
        },
        'bernoulliNB': {
            'model': BernoulliNB(),
            'params': {
                'alpha': [0.1, 0.5, 1.0],
                'binarize': [0.0, 0.5, 1.0]
            }
        },
        'decision_tree': {
            'model': DecisionTreeClassifier(),
            'params': {
                'max_depth': [None, 10, 20],
                'min_samples_split': [2, 5, 10],
                'criterion': ['gini', 'entropy']
            }
        },
        'knn': {
            'model': KNeighborsClassifier(),
            'params': {
                'n_neighbors': [3, 5, 7],
                'weights': ['uniform', 'distance'],
                'metric': ['euclidean', 'manhattan']
            }
        },
        'mlp': {
            'model': MLPClassifier(max_iter=500),
            'params': {
                'hidden_layer_sizes': [(50,), (100,), (100, 50)],
                'activation': ['relu', 'tanh'],
                'solver': ['adam', 'sgd'],
                'alpha': [0.0001, 0.001]
            }
        },
        'sgd': {
            'model': SGDClassifier(),
            'params': {
                'loss': ['hinge', 'log_loss'],
                'penalty': ['l2', 'l1', 'elasticnet'],
                'alpha': [0.0001, 0.001]
            }
        },
        'ridge': {
            'model': RidgeClassifier(),
            'params': {
                'alpha': [0.1, 1.0, 10.0]
            }
        },
        'adaboost': {
            'model': AdaBoostClassifier(),
            'params': {
                'n_estimators': [50, 100],
                'learning_rate': [0.5, 1.0]
            }
        },
        'gradient_boosting': {
            'model': GradientBoostingClassifier(),
            'params': {
                'n_estimators': [50, 100],
                'learning_rate': [0.05, 0.1],
                'max_depth': [3, 5]
            }
        }
    }

    results = []

    for name, mp in model_params.items():
        search = RandomizedSearchCV(mp['model'], mp['params'], cv=5, n_iter=10, scoring='f1', n_jobs=-1)
        search.fit(X_train, y_train)

        best_model = search.best_estimator_
        best_score = search.best_score_
        best_params = search.best_params_

        results.append({
            'model': name,
            'best_score': best_score,
            'best_params': best_params
        })

    df_results = pd.DataFrame(results, columns=['model', 'best_score', 'best_params'])
    df_results = df_results.sort_values(by='best_score', ascending=False).reset_index(drop=True)

    df_results.to_csv("model_comparison_results.csv", index=False)
    return df_results

evaluate_models()