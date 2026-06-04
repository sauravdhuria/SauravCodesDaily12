import pandas as pd

df =pd.read_csv('data.csv')

tall_pokemon=df[df["Height"]>=2]

print(f'Tall pokemon : \n{tall_pokemon}')

legendary =df[df['Legendary']==1]
print(f'Legendary : \n{legendary}')

ff=df[(df['Type1']=='Fire') &
      (df['Type2']=='Rock')]
print(f'Fighting : \n{ff}')
