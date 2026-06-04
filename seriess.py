import pandas as pd

# print(pd.__version__)
# data =[100,200,300,400,500]
#
# series=pd.Series(data,index=['a','b','c','d','e'])
# # print(series)
#
# # print(series.loc['a'])
# #
# # series.loc['c']=500
# # print(series.iloc[2])
# print(series[series<=200])

# use dict

calories={'Day 1':1750 ,'Day 2': 2100,'Day 3':1700}

series=pd.Series(calories)
print(series)
series.loc['Day 3'] +=500

print(series.loc['Day 3'])