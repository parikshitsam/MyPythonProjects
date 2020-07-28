#https://crime-data-explorer.fr.cloud.gov/downloads-and-docs
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Read Data

inequality = pd.read_csv("us inequality.txt",names = ["number","State","Gini"], sep ="\t", index_col=1)
crimes = pd.read_csv("us crime statistics.txt", sep ="\t",index_col=0, names=["State","City","Population","vc Total",
                                                       "vc Murder and Manslaughter", "vc Rape",'vc Robbery',
                                                       "vc Aggravated Assault","pc Total",'pc Burglary',
                                                       "pc Larceny","pc Motor vehicle theft","Arson"])

inequality.drop(columns="number", inplace=True)
crimes.reset_index(inplace=True)

def ineq(row):
    state = row["State"]
    x=0
    for character in state:
        if character.isdigit():
            state = state[:x]
            break
        x += 1

    row["Avg Inequality"] = inequality.loc[state, "Gini"]
    row["State"] = state
    return row
crimes = crimes.apply(ineq , axis=1)
print(len(inequality.index))
print(crimes.columns)

h=sns.jointplot(crimes["pc Total"],crimes["Avg Inequality"], kind="scatter", space=0)
#sns.pairplot(crimes[['Population', 'vc Total', 'vc Robbery', 'vc Aggravated Assault', 'pc Total',
#                     'pc Burglary', 'pc Larceny', 'pc Motor vehicle theft', 'Avg Inequality']], diag_kind='kde');
#plt.xlabel = "Property Crimes"
#plt.title("Economic Inequality and Crimes in US cities")
h.set_axis_labels('Crimes', 'Inequality')
h.fig.suptitle('Property Crimes and Inequality in the US')
plt.show()

# Combine Data


