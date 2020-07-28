import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

df1 = pd.read_csv('6_4.txt', sep = ' ', header=0, index_col=0, usecols= [0,1,2,3,4])
df2 = pd.read_csv('6_4.txt', sep = ' ', header=0, index_col=0, usecols= [5,6,7,8,9])
df = df1.append(df2)
print(df)
