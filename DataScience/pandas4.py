import pandas as pd

rf=pd.read_csv("sample_data.csv",parse_dates=['Day'])
print(type(rf.Day[0]))
rf.set_index("Day",inplace=True)
print(rf)
rf.fillna(0)
rf.fillna({
    'Age':rf.Age.mean(),
    'Name':'No name',
})
rf.fillna(method='ffill',limit=1) #Forward Fill
rf.fillna(method='bfill') #Backward Fill
print(rf.fillna(method='bfill',axis='columns')) #Backward Fill
print(rf.interpolate())
print(rf.dropna(how="all"))
print(rf.dropna(thresh=2)) #if only two valid value,keep it
# print(rf)