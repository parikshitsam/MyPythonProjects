
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np
from scipy import stats
from scipy.stats import t
from scipy.stats import norm
import matplotlib.colors

np.random.seed(12345)

df = pd.DataFrame([np.random.normal(32000,200000,3650), 
                   np.random.normal(43000,100000,3650), 
                   np.random.normal(43500,140000,3650), 
                   np.random.normal(48000,70000,3650)], 
                  index=[1992,1993,1994,1995])
df


# In[9]:

mean_df = df.mean(axis = 1)
q95 =1.96
n=3650
df_sd = np.array([200000,100000,140000,70000])
df_err1 = -q95*df_sd/n**(1/2)+mean_df
df_err2 = q95*df_sd/n**(1/2)+mean_df
error = df_err2 - df_err1


# In[10]:

#plt.figure()
# fig, ax = plt.subplots()
# ax.bar(df.index,mean_df, yerr=error, capsize=7)


# In[11]:

threshold = 42000


# In[12]:

prob = 1-norm.cdf((threshold-mean_df)*(n**(1/2))/df_sd)


# In[13]:

cmap = cmap = plt.cm.rainbow


# In[17]:

fig, ax = plt.subplots()
ax.bar(df.index,mean_df, yerr=error, capsize=7, color= cmap(prob))
ax.plot([1991.5, 1995.5], [threshold, threshold], "k--")
sm = plt.cm.ScalarMappable(cmap=cmap)
sm.set_array([])
fig.colorbar(sm)
ax.set_xticks(df.index)
ax.set_xlabel("Years")
ax.set_ylabel("Mean")
plt.gca().set_title('Confidence Interval for Mean')
plt.show()

