import pandas as pd
from matplotlib import pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import MinMaxScaler

df=pd.read_csv("income.csv")

plt.scatter(df['Age'],df['Income($)'])
plt.show()


scaler = MinMaxScaler()
df[['Age', 'Income($)']] = scaler.fit_transform(df[['Age', 'Income($)']])


kM=KMeans(n_clusters=3)
y_predicted=kM.fit_predict(df[['Age','Income($)']])
df['cluster']=y_predicted
print(y_predicted)

df0=df[df.cluster==0]
df1=df[df.cluster==1]
df2=df[df.cluster==2]
plt.scatter(df0['Age'],df0['Income($)'],color="blue")
plt.scatter(df1['Age'],df1['Income($)'],color="green")
plt.scatter(df2['Age'],df2['Income($)'],color="red")
plt.scatter(kM.cluster_centers_[:,0],kM.cluster_centers_[:,1],color="purple",marker="*",label='Centroid')
plt.xlabel("Age")
plt.ylabel("Income")
plt.legend()
plt.show()

k_range=range(1,11)
sse=[]
for k in k_range:
    km=KMeans(n_clusters=k)
    km.fit(df[['Age','Income($)']])
    sse.append(km.inertia_)
print(sse)
plt.xlabel("K")
plt.ylabel("SSE")
plt.plot(k_range,sse)
plt.show()


