"""
Dataframe = A tabular data structure with rows AND columns(2-Dimension)
"""
import pandas as pd

data = {'Name':['saurav','shinshan','abhishake','meow'], 'Age':[21,22,23,24]}
df = pd.DataFrame(data,index=['Employee 1','Employee 2','Employee 3','Employee 4'])
# print(df.loc['Employee 1'])


#Add a new column
df['Job']=['Cook','N/A','pogo','gandmasti']

print(df)
# Add a new row
new_row =pd.DataFrame({'Name':['Luffy','Nami','zoro','usop'], 'Age':[21,22,23,24]},index=['Joyboy','baddie','direction','sniper'])

df=pd.concat([df,new_row]) #the object at first will ocure first
print(df)