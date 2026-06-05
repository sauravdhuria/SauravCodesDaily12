import numpy as np
# Data cleaning = the po=rocess of fixing/removing :
#                 incomplete ,incorrect ,or irrelevent data.
#                 ~75 % of work done with Pandas is data cleaning

import pandas as pd
df = pd.read_csv("data.csv")

#drop irrelevant co;umn
# df= df.drop(columns=["Legendary"])
df=df.dropna(subset=["Type2"])
print(df.to_string())

#handle missing data
df=df.fillna({"Type2":"None"})
print(df.to_string())

#fix inconsistent values
df["Type1"]=df["Type1"].replace({"Grass":"GRASS","Fire":"FIRE","Water":"WATER"})

#fix data types
df["Legendary"]=df["legendary"].astype(bool)

#remove dupicate
df=df.drop_duplicates()