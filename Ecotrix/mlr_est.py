import statsmodels.api as sm
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
cols = "Observation GDP M2 CPI LTRATE TBRATE".split()
data = pd.read_csv("7_10.txt", sep = " ", names= cols)

data["lnM"] = np.log(data["M2"])
data["lnY"] = np.log(data['GDP'])
data["lnltr"] = np.log(data["LTRATE"])
data['lnstr'] = np.log(data["TBRATE"])
y = data["lnM"]
X = data[["lnY","lnltr"]]
X = sm.add_constant(X)
model = sm.OLS(y,X).fit()
print(model.summary())
# h = sns.pairplot(data[['lnM','lnY','lnltr','lnstr']])
# plt.show()