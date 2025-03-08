import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

##############################################
#Data Cleaning
df1=pd.read_csv("bengaluru_house_prices.csv")

print(df1.groupby('area_type')['area_type'].agg('count'))

df2=df1.drop(['area_type', 'availability', 'society', 'balcony'],axis=1)
print(df2.head())
print(df2.isnull().sum())
print(df2.shape)
df2.dropna(inplace=True)
print(df2.shape)

print(df2['size'].unique())
df2['bhk']=df2['size'].apply(lambda x: int(x.split(" ")[0]))
print(df2['bhk'].unique())

print(df2[df2.bhk>20])

def is_float(x):
    try:
        float(x)
    except:
        return False
    return True

print(df2[~df2['total_sqft'].apply(is_float)])

def convert_sqft_to_num(x):
    tokens=x.split('-')
    if len(tokens)==2:
        return (float(tokens[0])+float(tokens[1]))/2
    try:
        return float(x)
    except:
        return None

df3=df2.copy()
df3['total_sqft']=df3['total_sqft'].apply(convert_sqft_to_num)
print(df3.loc[30])
print("check: ",df3[~df3['total_sqft'].apply(is_float)])

##############################################
#Feature Engineering
df4=df3.copy()
df4['price_per_sqft']=df4['price']*100000/df4['total_sqft']
print(df4)

print(len(df4.location.unique()))
loc_group=df4.groupby('location')['location'].agg('count').sort_values(ascending=False)
print(loc_group)
print(len(loc_group[loc_group<=10]))

lesser=loc_group[loc_group<=10]
df5=df4.copy()
df5.location=df5['location'].apply(lambda x: 'others' if x in lesser else x)
print(len(df5.location.unique()))

print(df5[df5.total_sqft/df5.bhk<300].head())
df6=df5[~(df5.total_sqft/df5.bhk<300)]
print(df6.shape)

##############################################
#Outlier Detection & Removal
def remove_outliers(df):
    df_out=pd.DataFrame()
    for key,subdf in df.groupby('location'):
        m=np.mean(subdf.price_per_sqft)
        st=np.std(subdf.price_per_sqft)
        reduced_df=subdf[(subdf.price_per_sqft > (m-st)) & (subdf.price_per_sqft <= (m+st))]
        df_out=pd.concat([df_out,reduced_df],ignore_index=True)
    return df_out

print(df6.price_per_sqft.describe())
print(len(df6))
df7=remove_outliers(df6)
print(len(df7))

def plot_scatter_chart(df, location):
    bhk2 = df[(df.location==location) & (df.bhk==2)]
    bhk3 = df[(df.location==location) & (df.bhk==3)]
    plt.figure(figsize=(15,10))
    plt.scatter(bhk2.total_sqft,bhk2.price_per_sqft,color='blue',label='2 BHK',s=50)
    plt.scatter(bhk3.total_sqft,bhk3.price_per_sqft,color='green',marker='+',label='3 BHK',s=50)
    plt.xlabel("Total square feet area")
    plt.ylabel("price per square feet")
    plt.title(location)
    plt.legend()
    plt.show()
# plot_scatter_chart(df7,"Hebbal")

def remove_bhk_outliers(df):
    exclude_indices = np.array([])
    for location, location_df in df.groupby('location'):
        bhk_stats={}
        for bhk, bhk_df in location_df.groupby('bhk'):
            bhk_stats[bhk]={
                'mean':np.mean(bhk_df.price_per_sqft),
                'std':np.std(bhk_df.price_per_sqft),
                'count':bhk_df.shape[0]
            }
        for bhk,bhk_df in location_df.groupby('bhk'):
            stats=bhk_stats.get(bhk-1)
            if stats and stats['count']>5:
                exclude_indices=np.append(exclude_indices, bhk_df[bhk_df.price_per_sqft < (stats['mean'])].index.values)
    return df.drop(exclude_indices,axis='index')

df8=remove_bhk_outliers(df7)
print(df8.shape)
# plot_scatter_chart(df8,"Hebbal")


plt.hist(df8.price_per_sqft,rwidth=0.8)
plt.xlabel("Price per Square feet")
plt.ylabel("Count")
# plt.show()

df9=df8[df8.bath<df8.bhk+2]
print(df9.shape)

df10=df9.drop(['size','price_per_sqft'],axis=1)
print(df10.head())

##############################################
#Model Building

dummies=pd.get_dummies(df10.location)
df11=pd.concat([df10,dummies.drop('others',axis=1)],axis=1)
df12=df11.drop('location',axis=1)

X=df12.drop('price',axis=1)
Y=df12.price

from sklearn.model_selection import train_test_split
X_train,X_test,Y_train,Y_test=train_test_split(X,Y,test_size=0.2,random_state=10)

from sklearn.linear_model import LinearRegression
model=LinearRegression()
model.fit(X_train,Y_train)
print(model.score(X_test,Y_test))

from sklearn.model_selection import ShuffleSplit
from sklearn.model_selection import cross_val_score

cv=ShuffleSplit(n_splits=5,test_size=0.2,random_state=0)
score=cross_val_score(LinearRegression(),X,Y,cv=cv)
print(score.mean())

from sklearn.model_selection import GridSearchCV
from sklearn.linear_model import Lasso
from sklearn.tree import DecisionTreeRegressor

def find_best_algo(X,Y):
    algos={
        'linear_regression':{
            'model':LinearRegression(),
            'params': {
                'fit_intercept':[True,False]
            }
        },
        'lasso':{
            'model':Lasso(),
            'params': {
                'alpha':[1,2],
                'selection':['random','cyclic']
            }
        },
        'decision_tree':{
            'model':DecisionTreeRegressor(),
            'params': {
                'criterion':['squared_error', 'friedman_mse', 'absolute_error'],
                'splitter':['best','random']
            }
        }
    }
    scores=[]
    cv=ShuffleSplit(n_splits=5,test_size=0.2,random_state=0)
    for algo_name, config in algos.items():
        gs=GridSearchCV(config['model'],config['params'],cv=cv,return_train_score=False)
        gs.fit(X,Y)
        scores.append({
            'model':algo_name,
            'best_score':gs.best_score_,
            'best_params':gs.best_params_

        })
    return pd.DataFrame(scores,columns=['model','best_score','best_params'])
# ba=find_best_algo(X,Y)
# print(ba) #linear_regression    0.845847     {'fit_intercept': False}

def predict_price(location,sqft,bath,bhk):
    loc_index=np.where(X.columns==location)[0][0]

    x=np.zeros(len(X.columns))
    x[0]=sqft
    x[1]=bath
    x[2]=bhk
    if loc_index>=0:
        x[loc_index]=1
    return model.predict([x])[0]

print(predict_price('1st Phase JP Nagar',1000,2,2))
print(predict_price('Indira Nagar',1000,2,2))

##############################################
# Exporting to pickle file
import pickle
with open('blore_home_prices.pickle','wb') as f:
    pickle.dump(model,f)

import json
columns={
    'data_columns':[col.lower() for col in X.columns]
}
with open('columns.json','w') as f:
    f.write(json.dumps(columns))