import pandas as pd
import numpy as np
import xlrd

# # # Assignment 3 - More Pandas

# # ### Question 1 (20%)
# # Load the energy data from the file `Energy Indicators.xls`, which is a list of indicators of [energy supply and
# #renewable electricity production](Energy%20Indicators.xls) from the [United Nations]
# #(http://unstats.un.org/unsd/environment/excel_file_tables/2013/Energy%20Indicators.xls) for the year
# #2013, and should be put into a DataFrame with the variable name of **energy**.
# #
# # Keep in mind that this is an Excel file, and not a comma separated values file. Also, make sure to exclude
# #the footer and header information from the datafile. The first two columns are unneccessary, so you should get
# #rid of them, and you should change the column labels so that the columns are:
# # `['Country', 'Energy Supply', 'Energy Supply per Capita', '% Renewable']`
# # Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule).
# #For all countries which have missing data (e.g. data with "...") make sure this is reflected as `np.NaN` values.
# # Rename the following list of countries (for use in later questions):
# # ```"Republic of Korea": "South Korea",
# # "United States of America": "United States",
# # "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
# # "China, Hong Kong Special Administrative Region": "Hong Kong"```
# #
# # There are also several countries with numbers and/or parenthesis in their name. Be sure to remove these,
# # e.g.
# #
# # `'Bolivia (Plurinational State of)'` should be `'Bolivia'`,
# # `'Switzerland17'` should be `'Switzerland'`.
# #
# # <br>
# #
# # Next, load the GDP data from the file `world_bank.csv`, which is a csv containing countries' GDP from 1960
# #to 2015 from [World Bank](http://data.worldbank.org/indicator/NY.GDP.MKTP.CD). Call this DataFrame **GDP**.
# #
# # Make sure to skip the header, and rename the following list of countries:
# #
# # ```"Korea, Rep.": "South Korea",
# # "Iran, Islamic Rep.": "Iran",
# # "Hong Kong SAR, China": "Hong Kong"```
# #
# # <br>
# #
# # Finally, load the [Sciamgo Journal and Country Rank data for Energy Engineering and Power Technology]
# #(http://www.scimagojr.com/countryrank.php?category=2102) from the file `scimagojr-3.xlsx`, which ranks countries
# #based on their journal contributions in the aforementioned area. Call this DataFrame **ScimEn**.
# #
# # Join the three datasets: GDP, Energy, and ScimEn into a new dataset (using the intersection of country names).
# #Use only the last 10 years (2006-2015) of GDP data and only the top 15 countries by Scimagojr 'Rank' (Rank 1 through 15).
# #
# # The index of this DataFrame should be the name of the country, and the columns should be
# #['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
# #        'Citations per document', 'H index', 'Energy Supply',
# #        'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
# #        '2009', '2010', '2011', '2012', '2013', '2014', '2015'].
# #
# # *This function should return a DataFrame with 20 columns and 15 entries.*
#
# # In[ ]:
#
def keep_string(row):
    country = row["Country"]
    new_string = ""
    for char in country:
        if char.isdigit():
            break
        new_string = new_string + char

    if "(" in new_string:
        new_string = new_string[:new_string.index("(")]
    row["Country"] = new_string.strip()
    return row

test1 = pd.DataFrame({"Country":["India", "South Africa", "Brazil24", "Bolivia (Republic of)"],
                      "Energy Supply":[10,5,7,8],
                      "Energy Supply per capita": [2,4,3,1],
                      "% Renewable": [56,75,25,0]})

energy = pd.read_excel('Energy Indicators.xls', header = 16, nrows = (245 - 18), usecols ="C:G", index_col= 0)
colnames = ['Energy Supply', 'Energy Supply per Capita', '% Renewable']

#Create A Dictionary of Columns
dictcol ={}
val = 0
for col in energy.columns:
    dictcol[col] = colnames[val]
    val+=1


energy = energy.drop(energy.index[0]).rename(columns = dictcol)
energy.index.name = "Country"
energy["Energy Supply"] = pd.to_numeric(energy["Energy Supply"], errors='coerce')
energy['Energy Supply per Capita'] = pd.to_numeric(energy['Energy Supply per Capita'], errors='coerce')
# Convert `Energy Supply` to gigajoules (there are 1,000,000 gigajoules in a petajoule)
energy["Energy Supply"] *= 1000000
energy.reset_index(level=0, inplace=True)
energy = energy.apply(keep_string, axis=1)
energy.set_index('Country', inplace=True)
dict_cont = {"Republic of Korea": "South Korea",
             "United States of America": "United States",
             "United Kingdom of Great Britain and Northern Ireland": "United Kingdom",
             "China, Hong Kong Special Administrative Region": "Hong Kong"}
energy = energy.rename(dict_cont)

# Open GDP data file
GDP = pd.read_csv("world_bank.csv", skiprows=4, header=0, index_col=0)
gdp_rename_dict = {"Korea, Rep.": "South Korea",
                   "Iran, Islamic Rep.": "Iran",
                   "Hong Kong SAR, China": "Hong Kong"}
GDP.rename(gdp_rename_dict, inplace = True)

# Open Journal Ranking Datafile
ScimEn = pd.read_excel("scimagojr-3.xlsx", index_col=1)

final_data = energy.merge(GDP, how="inner", left_index=True, right_index=True)\
    .merge(ScimEn,how="inner", left_index=True, right_index=True)
all_cols = list(final_data.columns)

cols_to_keep = ['Rank', 'Documents', 'Citable documents', 'Citations', 'Self-citations',
                'Citations per document', 'H index', 'Energy Supply',
                'Energy Supply per Capita', '% Renewable', '2006', '2007', '2008',
                '2009', '2010', '2011', '2012', '2013', '2014', '2015']
cols_to_drop = []
for col in all_cols:
    if col not in cols_to_keep:
        cols_to_drop.append(col)

ans1 = final_data.drop(cols_to_drop, axis=1)
ans1 = ans1[ans1["Rank"] < 16]
def answer_one():
    return ans1
print(answer_one())
#
#
# # ### Question 2 (6.6%)
# # The previous question joined three datasets then reduced this to just the top 15 entries.
# # When you joined the datasets, but before you reduced this to the top 15 items, how many entries did you lose?

# # *This function should return a single number.*

def answer_two():
    return len(final_data) - len(ans1)

#
#
# # Answer the following questions in the context of only the top 15 countries by Scimagojr Rank
# #(aka the DataFrame returned by `answer_one()`)
# # ### Question 3 (6.6%)
# # What is the average GDP over the last 10 years for each country? (exclude missing values from this calculation.)
# # *This function should return a Series named `avgGDP` with 15 countries and their average
# # GDP sorted in descending order.*
def mean_gdp(row):
    years = row[['2006', '2007', '2008', '2009', '2010', '2011', '2012', '2013', '2014', '2015']]
    row["avgGDP"] = np.mean(years)
    return row

data =ans1
data = data.apply(mean_gdp,axis=1)
sorted_data = data.sort_values(by=["avgGDP"], ascending=False)
ans3 = sorted_data["avgGDP"]

def answer_three():
    return ans3

# # ### Question 4 (6.6%)
# # By how much had the GDP changed over the 10 year span for the country with the 6th largest average GDP?
# # *This function should return a single number.*
def answer_four():
    slargest = sorted_data.loc[sorted_data.index[5]]
    ans4 = slargest["2015"] - slargest["2006"]
    return ans4

# # ### Question 5 (6.6%)
# # What is the mean `Energy Supply per Capita`?
# #
# # *This function should return a single number.*
def answer_five():
    Top15 = answer_one()
    espc = Top15["Energy Supply per Capita"]
    return espc.mean()

#
# # ### Question 6 (6.6%)
# # What country has the maximum % Renewable and what is the percentage?
# #
# # *This function should return a tuple with the name of the country and the percentage.*
def answer_six():
    Top15 = answer_one()
    a = Top15.idxmax().loc["% Renewable"]
    return (a, Top15.loc[a,"% Renewable"])

#
#
# # ### Question 7 (6.6%)
# # Create a new column that is the ratio of Self-Citations to Total Citations.
# # What is the maximum value for this new column, and what country has the highest ratio?
# #
# # *This function should return a tuple with the name of the country and the ratio.*
def cit_ratio(row):
    ratio = row["Self-citations"] / row['Citations']
    row["citation_ratio"] = ratio
    return row
def answer_seven():
    Top15 = answer_one()
    Top15 = Top15.apply(cit_ratio, axis = 1)
    maxval = Top15.idxmax().loc["citation_ratio"]
    return (maxval,Top15.loc[maxval, "citation_ratio"])

#
# # ### Question 8 (6.6%)
# #
# # Create a column that estimates the population using Energy Supply and Energy Supply per capita.
# # What is the third most populous country according to this estimate?
# #
# # *This function should return a single string value.*
def popl(row):
    population = row["Energy Supply"]/row["Energy Supply per Capita"]
    row["population"] = population
    return row
def answer_eight():
    Top15 = answer_one()
    Top15 = Top15.apply(popl,axis = 1)
    return Top15.sort_values(by=["population"],ascending=False).index[2]

#
# # ### Question 9 (6.6%)
# # Create a column that estimates the number of citable documents per person.
# # What is the correlation between the number of citable documents per capita and the energy supply per capita? Use the `.corr()` method, (Pearson's correlation).
# #
# # *This function should return a single number.*
# #
# # *(Optional: Use the built-in function `plot9()` to visualize the relationship between Energy Supply per Capita vs. Citable docs per Capita)*


def answer_nine():
    Top15 = answer_one()
    Top15 = Top15.apply(popl,axis = 1)
    Top15["citations per capita"]= Top15.apply(lambda x: x.loc["Citations"]/x.loc["population"], axis = 1)
    return Top15.corr().loc["citations per capita", "Energy Supply per Capita"]

#
#
# # In[ ]:
#
#
# def plot9():
#     import matplotlib as plt
#     get_ipython().magic('matplotlib inline')
#
#     Top15 = answer_one()
#     Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
#     Top15['Citable docs per Capita'] = Top15['Citable documents'] / Top15['PopEst']
#     Top15.plot(x='Citable docs per Capita', y='Energy Supply per Capita', kind='scatter', xlim=[0, 0.0006])


#
#
# # In[ ]:
#
#
# #plot9() # Be sure to comment out plot9() before submitting the assignment!
#
#
# # ### Question 10 (6.6%)
# # Create a new column with a 1 if the country's % Renewable value is at or above the median for all
# # countries in the top 15, and a 0 if the country's % Renewable value is below the median.
# #
# # *This function should return a series named `HighRenew` whose index is the country name sorted in ascending order of rank.*
#
# # In[ ]:
data = answer_one()
median_r = data["% Renewable"].median()
def greater_than_equal_median(row):
    if row["% Renewable"]>= median_r:
        row["HighRenew"] = 1
    else:
        row["HighRenew"] = 0
    return row
def answer_ten():
    Top15 = answer_one()
    Top15 = Top15.apply(greater_than_equal_median,axis =1).sort_values(by =  ["Rank"], ascending= True)

    return Top15["HighRenew"]

#
# # ### Question 11 (6.6%)
# # Use the following dictionary to group the Countries by Continent,
# # then create a dateframe that displays the sample size
# # (the number of countries in each continent bin),
# # and the sum, mean, and std deviation for the estimated population of each country.
# #
# # ```python
ContinentDict  = {'China':'Asia',
                  'United States':'North America',
                  'Japan':'Asia',
                  'United Kingdom':'Europe',
                  'Russian Federation':'Europe',
                  'Canada':'North America',
                  'Germany':'Europe',
                  'India':'Asia',
                  'France':'Europe',
                  'South Korea':'Asia',
                  'Italy':'Europe',
                  'Spain':'Europe',
                  'Iran':'Asia',
                  'Australia':'Australia',
                  'Brazil':'South America'}
# # ```
# #
# # *This function should return a DataFrame with index named Continent `
# #['Asia', 'Australia', 'Europe', 'North America', 'South America']` and columns `['size', 'sum', 'mean', 'std']`*
#
# # In[ ]:
#
#
def answer_eleven():
    Top15 = answer_one()
    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    groups = Top15.groupby(ContinentDict).agg({"PopEst":["size","sum", "mean","std"]})
    groups.index.name = "Continent"
    return groups

#
#
# # ### Question 12 (6.6%)
# # Cut % Renewable into 5 bins. Group Top15 by the Continent, as well as these new % Renewable bins. How many countries are in each of these groups?
# #
# # *This function should return a __Series__ with a MultiIndex of `Continent`, then the bins for `% Renewable`. Do not include groups with no countries.*
#
# # In[ ]:
#

def answer_twelve():
    Top15 = answer_one()
    Top15["Rcat"] =pd.cut(Top15["% Renewable"],5)

    Top15['PopEst'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    groups = Top15.groupby([ContinentDict,"Rcat"]).size()
    groups.index.name = "Continent"
    return groups[groups >0]

#
#
# # ### Question 13 (6.6%)
# # Convert the Population Estimate series to a string with thousands separator (using commas). Do not round the results.
# #
# # e.g. 317615384.61538464 -> 317,615,384.61538464
# #
# # *This function should return a Series `PopEst` whose index is the country name and whose values are the population estimate string.*
#
# # In[ ]:
#
#
#e.g. 317615384.61538464 -> 317,615,384.61538464

def num_to_str(row):
    number = row["popsize"]
    num_string = str(number)
    dot_loc = num_string.index(".")
    num_commas = (dot_loc//3)
    skipdig = dot_loc%3
    comma_pos =[]
    result = ""
    for x in range(num_commas):
        if skipdig > 0:
            comma_pos.append(skipdig + (3*x))
        else:
            comma_pos.append(3*x)
    if comma_pos[0] != 0:
        comma_pos = [0] + comma_pos
    for x in range(len(comma_pos)-1):
        result = result + num_string[comma_pos[x]:comma_pos[x+1]]+","
    result = result + num_string[comma_pos[-1]:]
    row["PopEst"] = result
    return row
#print(num_to_str(317615384.61538464))
def answer_thirteen():
    Top15 = answer_one()
    Top15['popsize'] = Top15['Energy Supply'] / Top15['Energy Supply per Capita']
    Top15 = Top15.apply(num_to_str,axis = 1)
    return Top15["PopEst"]

#
#
# # ### Optional
# #
# # Use the built in function `plot_optional()` to see an example visualization.
#
# # In[ ]:
#
#
# def plot_optional():
#     import matplotlib as plt
#     get_ipython().magic('matplotlib inline')
#     Top15 = answer_one()
#     ax = Top15.plot(x='Rank', y='% Renewable', kind='scatter',
#                     c=['#e41a1c','#377eb8','#e41a1c','#4daf4a','#4daf4a','#377eb8','#4daf4a','#e41a1c',
#                        '#4daf4a','#e41a1c','#4daf4a','#4daf4a','#e41a1c','#dede00','#ff7f00'],
#                     xticks=range(1,16), s=6*Top15['2014']/10**10, alpha=.75, figsize=[16,6]);
#
#     for i, txt in enumerate(Top15.index):
#         ax.annotate(txt, [Top15['Rank'][i], Top15['% Renewable'][i]], ha='center')
#
#     print("This is an example of a visualization that can be created to help understand the data. This is a bubble chart showing % Renewable vs. Rank. The size of the bubble corresponds to the countries' 2014 GDP, and the color corresponds to the continent.")
#
#
# # In[ ]:
#
#
# #plot_optional() # Be sure to comment out plot_optional() before submitting the assignment!
#
