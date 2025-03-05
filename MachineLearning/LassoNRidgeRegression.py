import pandas as pd
df=pd.read_csv("Melbourne_housing_FULL.csv")
cols_to_use=['Suburb','Rooms','Type','Method','SellerG','Regionname','Propertycount',
             'Distance','CouncilArea','Bedroom2','Bathroom','Car','Landsize','BuildingArea','Price']
df=df[cols_to_use]
cols_to_fill_zero=['Propertycount','Distance','Bedroom2','Bathroom','Car']

df[cols_to_fill_zero]=df[cols_to_fill_zero].fillna(0)
df['Landsize']=df['Landsize'].fillna(df.Landsize.mean())
df['BuildingArea']=df['BuildingArea'].fillna(df.BuildingArea.mean())
df.dropna(inplace=True)
print(df.isna().any())
df=pd.get_dummies(df,drop_first=True)

x=df.drop('Price',axis=1)
y=df.Price


print(df)
from sklearn.model_selection import train_test_split
Xtrain,xtest,Ytrain,ytest=train_test_split(x,y,test_size=0.3,random_state=2)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(Xtrain,Ytrain)

from sklearn.linear_model import Lasso
lasso_reg=Lasso(alpha=50,max_iter=100,tol=0.1)
lasso_reg.fit(Xtrain,Ytrain)
print(lasso_reg.score(xtest,ytest)) #0.6636111369404489
from sklearn.linear_model import Ridge
ridge_reg=Ridge(alpha=50,max_iter=100,tol=0.1)
ridge_reg.fit(Xtrain,Ytrain)
print(ridge_reg.score(xtest,ytest)) #0.6670848945194958
