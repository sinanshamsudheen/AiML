import pandas as pd
rf=pd.read_csv("movies.csv",header=1,names=["helo","how","are","you","doing"],nrows=10,na_values=['not available','-1'])
print(rf)
rf["ratio"]=rf["how"]/rf["are"]
print(rf)

rf.to_csv("final.csv",index=False,header=False)
def standardize(curr):
    if curr=="INR":
        return "USD"
    return curr
movies_db=pd.read_excel("D:\IDM\Documents\movies-db-1.xlsx","movies")
finance_db=pd.read_excel("D:\IDM\Documents\movies-db-1.xlsx","financials",converters={'currency':standardize})

print(movies_db)
print(finance_db)

rf_merged=pd.merge(movies_db,finance_db,on = "movie_id")
print(rf_merged)

# rf_merged.to_excel("merged.xlsx",sheet_name="merged",index=False)

df=pd.DataFrame({ 
    "family":['john','jack','jill'],
    "friends":['joy','james','joseph'],
})
weather=pd.DataFrame({ 
    "day":['06/04/2004','08/04/2004','10/04/2004'],
    "temperature":[30,33,28],
})
print(df)
print(weather)

with pd.ExcelWriter("weather.xlsx") as writer:
    df.to_excel(writer,sheet_name="fam")
    weather.to_excel(writer,sheet_name="weather")
    