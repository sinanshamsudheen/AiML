import seaborn as sns
from matplotlib import pyplot as plt
import pandas as pd

# df=pd.read_excel("histograms.xlsx")
# print(df)

# s=sns.histplot(df["Exam_Score"],kde=True)
# s=sns.histplot(data=df,x="Exam_Score",kde=True)
# plt.xlabel("Score")
# plt.ylabel("Count")
# plt.title("Scores Histo")
# print(s)

df2=pd.read_excel("scatter_plot.xlsx")
t=sns.scatterplot(data=df2)
print(df2)
plt.show()