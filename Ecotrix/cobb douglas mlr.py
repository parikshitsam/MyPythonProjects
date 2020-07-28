import statsmodels.api as sm
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
cols = ["Year", "Real gross product", "Labor days", "Real capital input"]
df = pd.read_csv("7_3.txt", sep = " ", names=cols)
df["Real gross product"] = df["Real gross product"].str.replace(",",'').astype(float)
df["Real capital input"] = df["Real capital input"].str.replace(',','').astype(float)

df['lnY'] = np.log(df["Real gross product"])
df['lnX1'] = np.log(df['Labor days'])
df['lnX2'] = np.log(df['Real capital input'])

X = df[['lnX1', 'lnX2']]
y = df['lnY']
X= sm.add_constant(X)

model = sm.OLS(y,X).fit()
print(model.summary())