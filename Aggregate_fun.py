# Aggregate function is a funcction that reduces set of values into a single
# summary value used to summarize and analyze data , often used with groupby() function

import pandas as pd

df=pd.read_csv('data.csv')
#Whole dataframae

print(df.mean(numeric_only=True))
print(df.min(numeric_only=True))
print(df.max(numeric_only=True))
print(df.sum(numeric_only=True))
print(df.count())

#single column
print(df['Height'].mean(numeric_only=True))
print(df['Height'].min(numeric_only=True))
print(df['Height'].max(numeric_only=True))
print(df['Height'].sum(numeric_only=True))
print(df['Height'].count())


#groupby

group=df.groupby('Type1')
print(group.count())
print(group['Height'].mean(numeric_only=True))
print(group['Height'].min(numeric_only=True))
print(group['Height'].max(numeric_only=True))
print(group['Height'].sum(numeric_only=True))
print(group['Height'].count())