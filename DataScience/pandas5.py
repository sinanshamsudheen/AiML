import pandas as pd
import numpy as np

rf=pd.read_csv("sample_data.csv")
s=rf.replace(to_replace=[-9999,"Alice"],value=np.nan)
print(s)
t=rf.replace(to_replace={
    "Name" : "Bob",
    "Age" : 25,
    "City" : "New York"
},value=np.nan)
print(t)
p=rf.replace({
    "Denver" : "NotDenver",
    22:69,
})
print(p)
q=rf.replace(['Emily','Grace','Frank'],['NotEmily','NotFrank','NotGrace'])
print(q)