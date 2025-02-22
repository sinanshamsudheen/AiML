import pandas as pd

df=pd.read_csv("D:\VsCode\AiML\movies.csv")
# print(df)
print(df.head(4)) #first 4
print(df.tail(3)) #last 3

print(df.sample(4)) #Random samples

print(df[2:5])
print(df.shape)
print(dir(df.imdb_rating))

print(f"The minimum rating is: {df.imdb_rating.min()}")
print(f"The maximum rating is: {df.imdb_rating.max()}")
print(f"The average rating is: {df.imdb_rating.mean()}")

print(df[df.industry=="Bollywood"])
df_h = df[df.industry=="Hollywood"]
print(df_h)
