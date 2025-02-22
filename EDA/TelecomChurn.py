import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# %config InlineBackend.figure_format='retina'

df = pd.read_csv("churn-bigml-20.csv")

# 1- Let's see how churn rate is related to the International plan feature. We'll do this using a crosstab contingency table and 
# also through visual analysis with Seaborn (however, visual analysis will be covered more thoroughly in the next article).
ct=pd.crosstab(df["Churn"],df["International plan"])
print(ct)
sns.countplot(data=df,x="International plan",hue="Churn")

# 2- We see that, with International Plan, the churn rate is much higher, which is an interesting observation! Perhaps large and poorly
#  controlled expenses with international calls are very conflict-prone and lead to dissatisfaction among the telecom operator's customers.
# Next, let's look at another important feature – Customer service calls. Let's also make a summary table and a picture.
ct2=pd.crosstab(df["Churn"],df["Customer service calls"],margins=True)
print(ct2)
ct2.plot(kind="bar",legend=True,xlabel="Customer service calls")

# 3- Although it's not so obvious from the summary table, it's easy to see from the above plot that the churn rate increases sharply from 4 customer service calls and above.
# Now let's add a binary feature to our DataFrame – Customer service calls > 3. And once again, let's see how it relates to churn.
df["Many_service_calls"]=(df["Customer service calls"]>3).astype('int')
ct3=pd.crosstab(df["Churn"],df["Many_service_calls"])
sns.countplot(data=df,x="Many_service_calls",hue="Churn")
print(df)

# Let's construct another contingency table that relates Churn with both International plan and freshly created Many_service_calls.
ct4=pd.crosstab(df["International plan"] & df["Many_service_calls"] , df["Churn"])
print(ct4)
plt.show()

# Therefore, predicting that a customer is not loyal (Churn=1) in the case when the number of calls to the service center is greater 
# than 3 and the International Plan is added (and predicting Churn=0 otherwise), we might expect an accuracy of 85.8% (we are mistaken 
# only 464 + 9 times). This number, 85.8%, that we got through this very simple reasoning serves as a good starting point (baseline) for the further machine learning models that we will build.

