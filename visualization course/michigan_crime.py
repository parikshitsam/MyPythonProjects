import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn
import adspy_shared_utilities

inequality = pd.read_csv("WID_data_US-MI.csv",sep=";")
inequality = inequality[inequality["variable"]=="sptinc992t"]
inequality = inequality[inequality["percentile"] == "p95p100"]

crime = pd.read_csv("estimated_crimes_1979_2018_rev1.csv")
crime = crime[crime["state_abbr"] == "MI"]

df= crime.merge(inequality, how= "left", on="year", left_index=True)

fig, ax1 = plt.subplots()
#ax1.scatter(df["violent_crime"],df["value"])
ax2 = ax1.twinx()
ax1.plot(df["year"],df["property_crime"],"-", color = "red")
ax2.plot(df["year"],df["value"],"-")
ax1.set_xlabel("Year")
ax2.set_ylabel("Share of Top 5% in State Income")
ax1.set_ylabel("Number of Property Crimes", color = "red")
plt.title("Michigan Inequality and Crimes 1980:2015")
plt.show()
