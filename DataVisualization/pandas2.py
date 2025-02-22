import pandas as pd
rf = pd.read_csv("movies.csv")
print(rf.industry.unique())
print(rf.columns)

df= rf[["movie_id","title","industry"]]
print(df)


rls_yr=rf[(rf.release_year>2014) & (rf.industry=="Bollywood")]
print(rls_yr)

studs=rf.studio.unique()
print(studs)

movs=rf[rf.studio=='Marvel Studios']
print(movs)

print(rf.info())
print(rf[(rf.imdb_rating==rf.imdb_rating.max()) | (rf.imdb_rating==rf.imdb_rating.min())])

rf["age"]=rf.release_year.apply(lambda x: 2025-x)
print(rf)
# rf["profit"] = rf.apply(lambda x: x['revenue'] - x['budget'],axis=1)
rf.set_index("title",inplace=True)
print(rf.loc["Sholay"])
print(rf.iloc[2:6])

rf.reset_index(inplace=True)
print(rf)