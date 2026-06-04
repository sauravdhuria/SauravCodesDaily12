import pandas as pd

df = pd.read_csv('data.csv',index_col='Name')

# selection by column\
# print(df['Name'].to_string())

# print(df[['Name','Height','Weight']].to_string())


pokemon = input ('Enter a Pokemon name: ')
try :
    print(df.loc[pokemon])

except :
    print(f'{pokemon} not found')