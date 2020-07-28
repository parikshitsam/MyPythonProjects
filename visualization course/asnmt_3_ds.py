import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650),
                   np.random.normal(43000,100000,3650),
                   np.random.normal(43500,140000,3650),
                   np.random.normal(48000,70000,3650)],
                  index=[1992,1993,1994,1995])
mean_df = df.mean(axis = 1)
fig, ax = plt.subplots()
ax.bar(df.index,mean_df)
q95 =1.96
n=3650
print((-q95*200000/sqrt(n))+32000)