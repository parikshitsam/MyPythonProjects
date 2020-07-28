import pandas as pd
import numpy as np
#
census_df = pd.read_csv('census.csv')
census_df.head()
#
#
# def answer_seven():
#     largest_abschange = []
#     years_pop = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012',
#                  'POPESTIMATE2013', 'POPESTIMATE2014']
#     for i in range(len(census_df)):
#         current = census_df.iloc[i]
#         lst_diff = []
#         for x in years_pop:
#             for y in years_pop:
#                 lst_diff.append(abs(current[x]-current[y]))
#         largest_abschange.append(max(lst_diff))
#
#     # print(largest_abschange)
#     census_df["largest_abschange"] = largest_abschange
#     maxval = census_df["largest_abschange"].max()
#     county = census_df[census_df["largest_abschange"] == maxval]["CTYNAME"]
#
#
#     return county[county.index[0]]
#
#
# print(answer_seven())

#Create a query that finds the counties that belong to regions 1 or 2, whose name starts with
# 'Washington', and whose POPESTIMATE2015 was greater than their POPESTIMATE 2014.


# data = census_df[((census_df["REGION"] == 1) | (census_df["REGION"] == 2))
#                    & (census_df["POPESTIMATE2015"] > census_df["POPESTIMATE2014"])
#                    & (census_df['CTYNAME'].str.startswith('Washington'))]
# data = data[['STNAME', 'CTYNAME']]
# print(data)

# def answer_six():
#     rows_to_keep = []
#     for state in census_df["STATE"].unique():
#         state_data = census_df[census_df["STATE"] == state]
#         maxcounty = state_data.nlargest(3,"CENSUS2010POP")
#         rows_to_keep.append(maxcounty.index())
#     max_county_data = census_df.loc[rows_to_keep]
#     max_three = max_county_data.nlargest(3,"CENSUS2010POP")
#     #print(max_three)
#     return list(max_three["STNAME"])
#


state_pop = {} # Dict of states and their populations
data = census_df[census_df["SUMLEV"]==50]

for state in data["STNAME"].unique():
    newdata = data[data["STNAME"] == state]
    newdata = newdata.nlargest(3,"CENSUS2010POP")
    state_total = newdata["CENSUS2010POP"].sum()
    state_pop[state] = state_total

state_pop = {k: v for k, v in sorted(state_pop.items(), key=lambda item: item[1], reverse = True)}

print(list(state_pop.keys())[:3])




# data = data.sort_values(["STNAME", "CENSUS2010POP"], ascending=False)
# data = data.reset_index()
# data = data[["STNAME", "CENSUS2010POP"]]
# data = data.groupby("STNAME").head(3)
# data = data.groupby("STNAME").sum().sort_values("CENSUS2010POP", ascending = False).reindex()
# print(list(data.index[:3]))


#print(data)

# result = census_df.copy()
# result = result.reset_index()
# result = result[result['SUMLEV'] == 50]
# columns_to_keep = ['STNAME', 'CENSUS2010POP']
# result = result[columns_to_keep]
# result = result.sort_values(['STNAME', 'CENSUS2010POP'], ascending=False)
# result = result.groupby('STNAME').head(3)
# result = result.groupby("STNAME").sum().sort_values('CENSUS2010POP', ascending=False).reset_index()
# result = list(result['STNAME'].loc[:2])

# data = census_df[census_df["SUMLEV"] == 50].copy()
# years_pop = ['POPESTIMATE2010', 'POPESTIMATE2011', 'POPESTIMATE2012',
#                  'POPESTIMATE2013', 'POPESTIMATE2014']
# abs_diff = data[years_pop].max(axis = 1) - data[years_pop].min(axis = 1)
# data["abs_diff"] = abs_diff
# ser = data[data["abs_diff"] == data["abs_diff"].max()]
# county = ser["CTYNAME"].loc[ser.index[0]]

# print(county)
#

