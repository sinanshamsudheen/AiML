import pandas as pd
from sklearn.model_selection import train_test_split

df=pd.read_csv("spam.csv")
df['spam']=df.Category.apply(lambda x: 1 if x=="spam" else 0)
print(df)

X_train, X_test, Y_train, Y_test = train_test_split(df.Message,df.spam,test_size=0.25)

from sklearn.feature_extraction.text import CountVectorizer

v=CountVectorizer()

X_train_count=v.fit_transform(X_train.values)
print(X_train_count.toarray()[:3])

from sklearn.naive_bayes import MultinomialNB
model=MultinomialNB()
model.fit(X_train_count,Y_train)

emails=[
    "hello ash, can we hang out tomorrow?",
    "upto 20% discount on selected merchs!!"
]
email_count=v.transform(emails)
print(model.predict(email_count))
X_test_count=v.transform(X_test)
print(model.score(X_test_count,Y_test))

#we can replace the above code by using a pipeline!
from sklearn.pipeline import Pipeline
clf=Pipeline([
    ('vectorizer',CountVectorizer()),
    ('nb',MultinomialNB())
])
clf.fit(X_train,Y_train)
print(clf.score(X_test,Y_test))