
# coding: utf-8

# ---
# 
# _You are currently looking at **version 1.1** of this notebook. To download notebooks and datafiles, as well as get help on Jupyter notebooks in the Coursera platform, visit the [Jupyter Notebook FAQ](https://www.coursera.org/learn/python-data-analysis/resources/0dhYG) course resource._
# 
# ---

# In[ ]:


import pandas as pd
import numpy as np
import scipy.stats


# # Assignment 4 - Hypothesis Testing
# This assignment requires more individual learning than previous assignments - you are encouraged to check out the [pandas documentation](http://pandas.pydata.org/pandas-docs/stable/) to find functions or methods you might not have used yet, or ask questions on [Stack Overflow](http://stackoverflow.com/) and tag them as pandas and python related. And of course, the discussion forums are open for interaction with your peers and the course staff.
# 
# Definitions:
# * A _quarter_ is a specific three month period, Q1 is January through March, Q2 is April through June, Q3 is July through September, Q4 is October through December.
# * A _recession_ is defined as starting with two consecutive quarters of GDP decline, and ending with two consecutive quarters of GDP growth.
# * A _recession bottom_ is the quarter within a recession which had the lowest GDP.
# * A _university town_ is a city which has a high percentage of university students compared to the total population of the city.
# 
# **Hypothesis**: University towns have their mean housing prices less effected by recessions. Run a t-test to compare the ratio of the mean price of houses in university towns the quarter before the recession starts compared to the recession bottom. (`price_ratio=quarter_before_recession/recession_bottom`)
# 
# The following data files are available for this assignment:
# * From the [Zillow research data site](http://www.zillow.com/research/data/) there is housing data for the United States. In particular the datafile for [all homes at a city level](http://files.zillowstatic.com/research/public/City/City_Zhvi_AllHomes.csv), ```City_Zhvi_AllHomes.csv```, has median home sale prices at a fine grained level.
# * From the Wikipedia page on college towns is a list of [university towns in the United States](https://en.wikipedia.org/wiki/List_of_college_towns#College_towns_in_the_United_States) which has been copy and pasted into the file ```university_towns.txt```.
# * From Bureau of Economic Analysis, US Department of Commerce, the [GDP over time](http://www.bea.gov/national/index.htm#gdp) of the United States in current dollars (use the chained value in 2009 dollars), in quarterly intervals, in the file ```gdplev.xls```. For this assignment, only look at GDP data from the first quarter of 2000 onward.
# 
# Each function in this assignment below is worth 10%, with the exception of ```run_ttest()```, which is worth 50%.

# In[ ]:


# Use this dictionary to map state names to two letter acronyms
states = {'OH': 'Ohio', 'KY': 'Kentucky', 'AS': 'American Samoa', 'NV': 'Nevada', 'WY': 'Wyoming', 'NA': 'National', 'AL': 'Alabama', 'MD': 'Maryland', 'AK': 'Alaska', 'UT': 'Utah', 'OR': 'Oregon', 'MT': 'Montana', 'IL': 'Illinois', 'TN': 'Tennessee', 'DC': 'District of Columbia', 'VT': 'Vermont', 'ID': 'Idaho', 'AR': 'Arkansas', 'ME': 'Maine', 'WA': 'Washington', 'HI': 'Hawaii', 'WI': 'Wisconsin', 'MI': 'Michigan', 'IN': 'Indiana', 'NJ': 'New Jersey', 'AZ': 'Arizona', 'GU': 'Guam', 'MS': 'Mississippi', 'PR': 'Puerto Rico', 'NC': 'North Carolina', 'TX': 'Texas', 'SD': 'South Dakota', 'MP': 'Northern Mariana Islands', 'IA': 'Iowa', 'MO': 'Missouri', 'CT': 'Connecticut', 'WV': 'West Virginia', 'SC': 'South Carolina', 'LA': 'Louisiana', 'KS': 'Kansas', 'NY': 'New York', 'NE': 'Nebraska', 'OK': 'Oklahoma', 'FL': 'Florida', 'CA': 'California', 'CO': 'Colorado', 'PA': 'Pennsylvania', 'DE': 'Delaware', 'NM': 'New Mexico', 'RI': 'Rhode Island', 'MN': 'Minnesota', 'VI': 'Virgin Islands', 'NH': 'New Hampshire', 'MA': 'Massachusetts', 'GA': 'Georgia', 'ND': 'North Dakota', 'VA': 'Virginia'}

def keep_string(string):
    country = string
    new_string = ""
    minindex = len(country)

    if "[" in country:
        minindex = country.index("[")
    if "(" in country:
        minindex = min(country.index("("),minindex)

    new_string = country[:minindex]
    row = new_string.strip()
    return row




def get_list_of_university_towns():
    '''Returns a DataFrame of towns and the states they are in from the
    university_towns.txt list. The format of the DataFrame should be:
    DataFrame( [ ["Michigan", "Ann Arbor"], ["Michigan", "Yipsilanti"] ],
    columns=["State", "RegionName"]  )

    The following cleaning needs to be done:

    1. For "State", removing characters from "[" to the end.
    2. For "RegionName", when applicable, removing every character from " (" to the end.
    3. Depending on how you read the data, you may need to remove newline character '\n'. '''
    utowns = open("university_towns.txt", "r")
    lines = utowns.readlines()
    dict_towns = []
    utowns.close()
    for obj in lines:
        if "[edit]" in obj:
            accum = keep_string(obj)
        else:
            dict_towns.append([accum, keep_string(obj)])
    data = pd.DataFrame(dict_towns,columns=["State", "RegionName"]  )
    return data
#print(get_list_of_university_towns())
gdpdata = pd.read_excel("gdplev.xls", skiprows= 220, parse_cols= "E,G",nrows = 286-221, header = None)

gdpdata.columns = ["quarter","gdp"]

gdpdata["gdpgrowth"] = gdpdata["gdp"].pct_change()


def get_recession_start():
    '''Returns the year and quarter of the recession start time as a 
    string value in a format such as 2005q3'''
    df = gdpdata
    df["gdpgrowth"] = df["gdp"].pct_change()
    x = df["gdpgrowth"]
    restart = []
    for i, row in df.iterrows():
        if i == df.index[-1]:
            continue
        if (x[i]< 0) & (x[i+1]<0):
            restart.append(df.index[i])


    return df.loc[restart[0],"quarter"]
#print(get_recession_start())



def get_recession_end():
    '''Returns the year and quarter of the recession end time as a 
    string value in a format such as 2005q3'''
    df = gdpdata
    df["gdpgrowth"] = df["gdp"].pct_change()
    x = df["gdpgrowth"]
    restart = False

    for i, row in df.iterrows():
        if i == df.index[-1]:
            continue
        if (x[i]< 0) & (x[i+1]<0):
            restart =True
        if (restart) & (x[i] >= 0) & (x[i+1]>=0):
            reend = df.loc[i,"quarter"]
            break

    return reend




def get_recession_bottom():
    '''Returns the year and quarter of the recession bottom time as a 
    string value in a format such as 2005q3'''
    df = gdpdata
    df["gdpgrowth"] = df["gdp"].pct_change()
    x = df["gdpgrowth"]
    restarty = False


    for i, row in df.iterrows():
        if i == df.index[-1]:
            continue
        if (x[i]< 0) & (x[i+1]<0):
            restarty =True
            restart_index = i
        if (restarty) & (x[i] >= 0) & (x[i+1]>=0):
            reend_index = i
            break
    rec_series = df.loc[restart_index:reend_index]
    bottom_id = rec_series["gdp"].idxmin()
    bottom = rec_series.loc[bottom_id,"quarter"]
    return bottom
#print(get_recession_bottom())


# In[ ]:
# housing_data = pd.read_csv("City_Zhvi_AllHomes.csv")
# # housing_data["2000q1"] = housing_data["2000-01"]+housing_data["2000-02"]+housing_data["2000-03"]
# # print(housing_data["2000q1"])
# cols_to_keep = ["RegionName","State"]
# for year in range(2000,2017):
#     for x in range(1,5):
#         if x==1:
#             cols_to_keep.append(str(year)+"q"+str(x))
#             housing_data[str(year)+"q"+str(x)] = (housing_data[str(year)+"-01"]+\
#                                                  housing_data[str(year)+"-02"]+\
#                                                  housing_data[str(year)+"-03"])/3
#         elif x==2:
#             cols_to_keep.append(str(year) + "q" + str(x))
#             housing_data[str(year)+"q"+str(x)] = (housing_data[str(year)+"-04"]+\
#                                                  housing_data[str(year)+"-05"]+\
#                                                  housing_data[str(year)+"-06"])/3
#         elif x ==3:
#             cols_to_keep.append(str(year) + "q" + str(x))
#             if year==2016:
#                 housing_data["2000q1"] = (housing_data["2016-07"] + housing_data["2016-08"])/2
#                 break
#             housing_data[str(year)+"q"+str(x)] = (housing_data[str(year) + "-07"] + \
#                                                  housing_data[str(year) + "-08"] + \
#                                                  housing_data[str(year) + "-09"])/3
#         elif x==4:
#             if year==2016:
#                 break
#             cols_to_keep.append(str(year) + "q" + str(x))
#             housing_data[str(year)+"q"+str(x)] = (housing_data[str(year) + "-10"] + \
#                                                  housing_data[str(year) + "-11"] + \
#                                                  housing_data[str(year) + "-12"])/3

def convert_housing_data_to_quarters():
    '''Converts the housing data to quarters and returns it as mean 
    values in a dataframe. This dataframe should be a dataframe with
    columns for 2000q1 through 2016q3, and should have a multi-index
    in the shape of ["State","RegionName"].
    
    Note: Quarters are defined in the assignment description, they are
    not arbitrary three month periods.
    
    The resulting dataframe should have 67 columns, and 10,730 rows.
    '''
    housing_data = pd.read_csv("City_Zhvi_AllHomes.csv")
    # housing_data["2000q1"] = housing_data["2000-01"]+housing_data["2000-02"]+housing_data["2000-03"]
    # print(housing_data["2000q1"])
    cols_to_keep = ["RegionName", "State"]
    for year in range(2000, 2017):
        for x in range(1, 5):
            if x == 1:
                cols_to_keep.append(str(year) + "q" + str(x))
                housing_data[str(year) + "q" + str(x)] = (housing_data[str(year) + "-01"] + \
                                                          housing_data[str(year) + "-02"] + \
                                                          housing_data[str(year) + "-03"]) / 3
            elif x == 2:
                cols_to_keep.append(str(year) + "q" + str(x))
                housing_data[str(year) + "q" + str(x)] = (housing_data[str(year) + "-04"] + \
                                                          housing_data[str(year) + "-05"] + \
                                                          housing_data[str(year) + "-06"]) / 3
            elif x == 3:
                cols_to_keep.append(str(year) + "q" + str(x))
                if year == 2016:
                    housing_data["2016q3"] = (housing_data["2016-07"] + housing_data["2016-08"]) / 2
                    break
                housing_data[str(year) + "q" + str(x)] = (housing_data[str(year) + "-07"] + \
                                                          housing_data[str(year) + "-08"] + \
                                                          housing_data[str(year) + "-09"]) / 3
            elif x == 4:
                if year == 2016:
                    break
                cols_to_keep.append(str(year) + "q" + str(x))
                housing_data[str(year) + "q" + str(x)] = (housing_data[str(year) + "-10"] + \
                                                          housing_data[str(year) + "-11"] + \
                                                          housing_data[str(year) + "-12"]) / 3

    df = housing_data[cols_to_keep]

    df.set_index(["State","RegionName"], inplace=True)
    
    return df
#print(convert_housing_data_to_quarters())


# In[ ]:


def run_ttest():
    '''First creates new data showing the decline or growth of housing prices
    between the recession start and the recession bottom. Then runs a ttest
    comparing the university town values to the non-university towns values, 
    return whether the alternative hypothesis (that the two groups are the same)
    is true or not as well as the p-value of the confidence. 
    
    Return the tuple (different, p, better) where different=True if the t-test is
    True at a p<0.01 (we reject the null hypothesis), or different=False if 
    otherwise (we cannot reject the null hypothesis). The variable p should
    be equal to the exact p value returned from scipy.stats.ttest_ind(). The
    value for better should be either "university town" or "non-university town"
    depending on which has a lower mean price ratio (which is equivilent to a
    reduced market loss).'''
    utowns = get_list_of_university_towns()
    utowns["university_town"]=True
    utowns.set_index(["State", "RegionName"], inplace=True)
    #utowns["Statename"] = utowns["State"].apply(lambda x:states[x])
    housing_data = convert_housing_data_to_quarters()
    housing_data.reset_index(inplace=True)
    housing_data["Statecode"] = housing_data["State"]
    housing_data["State"] = housing_data["Statecode"].apply(lambda x:states[x])
    housing_data["rec_growth"] = housing_data[get_recession_start()]/housing_data[get_recession_bottom()]
    housing_data.set_index(["State", "RegionName"], inplace=True)
    df = housing_data.merge(utowns,how="left", left_index=True,right_index=True)
    uni_town_data = df[df["university_town"]==True]
    non_uni_town_data = df[df["university_town"]!=True]
    #housing_data.merge(utowns,how=right,)
    st,p = scipy.stats.ttest_ind(uni_town_data["rec_growth"].values,non_uni_town_data["rec_growth"].values,nan_policy='omit')
    if st<0:
        better = "university town"
    else:
        better = "non-university town"

    different = p<0.01

    return different,p,better
# print(run_ttest())
