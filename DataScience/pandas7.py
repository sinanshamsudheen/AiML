import pandas as pd
india_weather = pd.DataFrame({
    "city" : ["mumbai", "delhi", "banglore"],
    "temperature":[32,45,30],
    "humidity":[80,60,78]
})
print(india_weather)

us_weather = pd.DataFrame({
    "city" : ["new york", "chicago", "orlando"],
    "temperature":[21,14,35],
    "humidity":[68,65,75]
})
print(us_weather)

df=pd.concat([india_weather,us_weather])
print(df)
df2=pd.concat([india_weather,us_weather],keys=["india","us"])
print(df2)
print(df2.loc["india"])

temperature_df=pd.DataFrame({
    "city" : ["mumbai", "delhi", "banglore"],
    "temperature":[32,45,30],
},index=[0,1,2])

windspeed_df=pd.DataFrame({
    "city":["delhi","mumbai"],
    "windspeed":[7,12]
},index=[1,0])

t1=pd.concat([temperature_df,windspeed_df],axis=1)
t2=pd.concat([temperature_df,windspeed_df],axis=1)
print(t1)
print(t2)
t3=pd.merge(temperature_df,windspeed_df, on="city",how="full outer")
print(t3)