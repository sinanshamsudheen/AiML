# Download heart disease dataset heart.csv in Exercise folder and do following, (credits of dataset: https://www.kaggle.com/fedesoriano/heart-failure-prediction)

#     Load heart disease dataset in pandas dataframe
#     Remove outliers using Z score. Usual guideline is to remove anything that has Z score > 3 formula or Z score < -3
#     Convert text columns to numbers using label encoding and one hot encoding
#     Apply scaling
#     Build a classification model using support vector machine. Use standalone model as well as Bagging model and check if you see any difference in the performance.
#     Now use decision tree classifier. Use standalone model as well as Bagging and check if you notice any difference in performance
#     Comparing performance of svm and decision tree classifier figure out where it makes most sense to use bagging and why. Use internet to figure out in what conditions bagging works the best.


import pandas as pd
df=pd.read_csv("heart.csv")


# EDA
# print(df.isnull().sum())
# print(df.describe())
# print(df.HeartDisease.value_counts())

numeric_columns = df.select_dtypes(include=['float64', 'int64']).columns
df_no_outlier = df.copy()

for column in numeric_columns:
	if column != 'HeartDisease':
		z_score = (df[column] - df[column].mean()) / df[column].std()
		df_no_outlier = df_no_outlier[(z_score < 3) & (z_score > -3)]

# print(df.shape[0] - df_no_outlier.shape[0])
print(df.dtypes)
cols_to_dummy=df.select_dtypes('object').columns
print(cols_to_dummy)
df_no_outlier=pd.get_dummies(df,drop_first=True)
print(df_no_outlier)

X=df_no_outlier.drop('HeartDisease',axis=1)
Y=df.HeartDisease

from sklearn.preprocessing import StandardScaler
scaler=StandardScaler()
X_scaled=scaler.fit_transform(X)

from sklearn.model_selection import train_test_split
X_train, X_test, Y_train, Y_test = train_test_split(X_scaled,Y,test_size=0.2,random_state=10)

from sklearn.svm import SVC
svc_model=SVC(gamma='auto')
svc_model.fit(X_train,Y_train)
print("svc score: ",svc_model.score(X_test,Y_test))

from sklearn.model_selection import cross_val_score
scores_svc= cross_val_score(SVC(gamma='auto'),X_scaled,Y,cv=5)
print("cross val score svm: ",scores_svc.mean())

from sklearn.ensemble import BaggingClassifier
bagging_model=BaggingClassifier(
	estimator=SVC(gamma='auto'),
	n_estimators=100,
	random_state=0,
	max_samples=0.8,
	oob_score=True
)
bagging_model.fit(X_train,Y_train)
print("svc oob score: ",bagging_model.oob_score_)
print("svc score bagging: ",bagging_model.score(X_test,Y_test))

from sklearn.tree import DecisionTreeClassifier
tree_model=DecisionTreeClassifier()
tree_model.fit(X_train,Y_train)
print("DT score: ",tree_model.score(X_test,Y_test))

scores_dt=cross_val_score(DecisionTreeClassifier(),X_scaled,Y,cv=5)
print("DT cross val score: ",scores_dt.mean())

bagging_model2=BaggingClassifier(
	estimator=DecisionTreeClassifier(),
	n_estimators=100,
	random_state=0,
	max_samples=0.8,
	oob_score=True
)
bagging_model2.fit(X_train,Y_train)
print("DT oob score: ",bagging_model2.oob_score_)
print("DT score bagging: ",bagging_model2.score(X_test,Y_test))



