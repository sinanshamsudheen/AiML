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
    "upto 20% discount on selected merchs!!",
    "Dear User, You have been randomly selected as a lucky winner of the latest iPhone 15 Pro Max in our 2025 Global Apple Giveaway!  To claim your prize, simply click the link below and complete a short survey: Claim Your iPhone Now Hurry! This exclusive offer is valid for the next 24 hours only. Note: This promotion is for selected users only. Failure to respond will result in forfeiture of your reward.    Best regards,   Apple Promo Team   This is a promotional email. No purchase necessary. Terms & conditions apply.",
    "Dear Participant,Thank you for registering for the Summer of Code program! We are thrilled to have you on board and look forward to seeing your innovative ideas come to lifeAs the next step, you are required to submit a presentation outlining your approach to the problem statement. We’re giving you access to all the problem statements here: https://bit.ly/4jFyPHHowever, we request you to prioritize the domain you selected while filling out the form. You can provide approaches for up to three problem statements. Please prepare your presentation in PowerPoint (PPT) format and submit it via the Google Form linked below. Please ensure you submit your PPT before the presentation deadlineSubmission Form: https://bit.ly/42F84MImportant Info    Presentation Dates: 28th or 29th April 202    We’ll get back to you with the exact presentation time and meeting link closer to the dateNote    In case an individual participant has chosen a problem statement that ideally requires a team, we may pair them with another participant working on the same or similar idea    If multiple teams choose the same problem statement, we might assign alternative problem statements to ensure balanced distribution and fair evaluationIf you have any questions or need assistance, please message us at +91 86579 47489 or reply to this emailThanks once again for your enthusiasm. We’re excited to see what you come up withBest regardsIITB Trust Lab Team",
    "Dear Winner,Your email ID was selected in the International Mega Lottery 2025 Draw and you have won a cash prize of ₹50,00,000To claim your winnings, reply with your full name, bank details, and addressThis is a once-in-a-lifetime opportunity. Respond within 48 hours to avoid disqualificationSincerelyMr. Paul RaymonClaim Agent – Mega Lottery International",
    "Dear Customer,Due to recent suspicious activities, we require you to verify your account informationPlease login using the secure link below to prevent your account from being lockedVerify NoThank youState Bank of India Security Team"
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
print(clf.predict(emails))
print(clf.score(X_test,Y_test)*100)