import pandas as pd
import csv

df=pd.read_csv("final.csv")
print(df.shape)
del df["temp_planet_date"]

del df["temp_planet_mass"]

del df["pl_letter"]
del df["pl_name"]
del df["pl_controvflag"]
del df["pl_pnum"]
del df["pl_orbper"]
del df["pl_orbpererr1"]
del df["pl_orbpererr2"]
del df["pl_orbeccen"]
del df["pl_orbeccenerr1"]
del df["pl_orbeccenerr2"]
del df["pl_orbeccenlim"]
del df["pl_bmassj"]
del df["pl_bmassjerr1"]
del df["pl_bmassjerr2"]

print(df.shape)

print(list(df))
df=df.rename({
    'pl_hostname':"solarSystemname",
    'pl_discmethod':"planetdiscoverymethod",
    'pl_orbincl':"planetobitalinclination",
})

print(list(df))
df.to_csv('main.csv')

















