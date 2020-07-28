import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns
import statsmodels.api as sm

df = pd.read_csv('API_BGD_DS2_en_csv_v2_1224638.csv',header=2)
plt.style.use('fivethirtyeight')


exportdf = df[df['Indicator Name'].str.contains('export')]
# index : 156,194,485,641,921,1101,752,1105,1317
cols = list(range(2000,2019))
osdf = df.loc[[156,194,485,641,921,1101,752,1105,1317],]
osdf = osdf.drop(['Country Name','Country Code','Indicator Code'], axis=1)
osdf.set_index('Indicator Name', inplace=True)
osdf= osdf.T

import matplotlib.ticker as tick
def currency(x, pos):
    """The two args are the value and tick position"""
    if x >= 1e6:
        s = '${:1.1f}M'.format(x*1e-6)
    else:
        s = '${:1.0f}K'.format(x*1e-3)
    return s

formatter = tick.FuncFormatter(currency)
def functionplot(colname,divby,xlab,ylab,title):
    plt.figure(figsize=(9,7))
    plt.plot(osdf[colname]/divby)
    plt.xticks(rotation=70)
    plt.ylabel(xlab)
    plt.xlabel(ylab)
    plt.title(title)
    return


x = osdf.index[:-1]
y = list(osdf['ICT service exports (BoP, current US$)'])
y = y[:-1]
x = pd.to_datetime(x).year
x

fig, ax = plt.subplots(figsize=(8, 8))
def tutorial_temp(ax,x,y,xtick_list,xlabel,ylabel):
    ax.plot(x,y)
    labels = ax.get_xticklabels()
    plt.setp(labels, rotation=45, horizontalalignment='right')

    def value(x, pos):
        """The two args are the value and tick position"""
        if x >= 1e9:
            s = '${:1.1f}B'.format(x*1e-9)
        else:
            s = '${:1.0f}M'.format(x*1e-6)
        return s

    formatter = tick.FuncFormatter(value)

    # Now we'll move our title up since it's getting a little cramped
    # ax.title.set(y=1.05)

    ax.set(xlabel=xlabel, ylabel=ylabel)
    ax.yaxis.set_major_formatter(formatter)
    ax.set_xticks(xtick_list)
    #fig.subplots_adjust(right = 1)
xtick = list(range(1996,2018,2))
tutorial_temp(ax,x,y,xtick,'Year','Value','ICT exports')


fig, ((ax1,ax2),(ax3,ax4)) = plt.subplots(2,2,figsize=(9,9))
y1 = list(osdf['Service exports (BoP, current US$)'])[:-1]
y2= list(osdf['Commercial service exports (current US$)'])[:-1]
y3= list(osdf['ICT service exports (BoP, current US$)'])[:-1]
y4= list(osdf['High-technology exports (current US$)'])[:-1]
xtick1 = list(range(1978,2020,8))
xtick2 = list(range(1978,2019,8))
xtick3 = list(range(1996,2018,4))
xtick4 = list(range(2008,2016,))
tutorial_temp(ax1,x,y1,xtick1,'Year','Service exports')
tutorial_temp(ax2,x,y2,xtick2,'Year','Commercial service exports')
tutorial_temp(ax3,x,y3,xtick3,'Year','ICT exports')
tutorial_temp(ax4,x,y4,xtick4,'Year','High-technology exports')
fig.tight_layout()

# functionplot('ICT service exports (BoP, current US$)',1e8,'in billion dollars','Year',
#              'ICT service exports (BoP, current US$)')
# functionplot('Service exports (BoP, current US$)',1e8,'in billion dollars','Year','Service exports')


plt.show()