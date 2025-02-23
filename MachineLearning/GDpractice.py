import numpy as np
import pandas as pd

df=pd.read_csv("test_scores.csv")

def gradient_descent(x,y):
    b_curr=m_curr=0
    iterations=10000
    learning_rate=0.0002
    n=len(x)

    for i in range(iterations):
        y_predicted=m_curr*x + b_curr
        cost=(1/n)*sum([val**2 for val in (y-y_predicted)])
        md=-(2/n)*sum(x*(y-y_predicted))
        bd=-(2/n)*sum((y-y_predicted))
        m_curr=m_curr-learning_rate*md
        b_curr=b_curr-learning_rate*bd
        print("m: {},b: {},cost: {}, iteration: {}".format(m_curr,b_curr,cost,i))

x=np.array(df.math)
y=np.array(df.cs)
gradient_descent(x,y)
# m: 1.0390524972633637,b: 0.4045913382155772,cost: 31.735517659560408, iteration: 9999