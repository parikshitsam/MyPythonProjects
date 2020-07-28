import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

df = pd.read_csv('7_11.txt', sep = ' ', names = ['Observation','output','capital',
                                                 'labor',
                                                 'capital to labor ratio'],
                 index_col=0)

plt.plot(df['output'],'-o')
sns.pairplot(df)
plt.show()