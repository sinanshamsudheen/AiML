import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df=pd.read_csv("height_weight.csv")

df.drop('weight',axis=1,inplace=True)
print(df.head())

plt.hist(df.height,bins=20,rwidth=0.8)
plt.xlabel("Height(inches)")
plt.ylabel('count')
plt.show()

print(df.height.mean())
print(df.height.std())

upper_limit=df.height.mean() + 3*df.height.std()
lower_limit=df.height.mean() - 3*df.height.std()
print(df[(df.height>upper_limit) | (df.height<lower_limit)])

df_no_outlier_std_dev=df[(df.height<upper_limit) & (df.height>lower_limit)]
df['zscore']=(df.height-df.height.mean())/df.height.std()
print(df.head())

df_no_outlier_zscore=df[(df.zscore<3) & (df.zscore>-3)]
print(df.shape[0]-df_no_outlier_zscore.shape[0])