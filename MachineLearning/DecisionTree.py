import pandas as pd

from sklearn import tree
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder

df=pd.read_csv("salaries.csv")
inputs=df.drop('salary_more_then_100k',axis='columns')
target=df['salary_more_then_100k']
print(inputs)

company_le=LabelEncoder()
job_le=LabelEncoder()
degree_le=LabelEncoder()

inputs['company_n']=company_le.fit_transform(inputs['company'])
inputs['job_n']=company_le.fit_transform(inputs['job'])
inputs['degree_n']=company_le.fit_transform(inputs['degree'])

inputs_n=inputs.drop([ 'company','job','degree'],axis=1)
print(inputs_n)
model=tree.DecisionTreeClassifier()

X_train, X_test, Y_train, Y_test = train_test_split(inputs_n,target,test_size=0.2)
model.fit(X_train,Y_train)
print("score: ",model.score(X_test,Y_test))
print(model.predict("Prediction: ",[[2,0,1]]))

