import pandas as pd
df = pd.read_csv("nomre.csv")
jam = df["grade"].sum()
kam = df["grade"].min()
bishtar = df["grade"].max()
miangin = df["grade"].mean()
print("miangin =",miangin)
print("bishtar =",bishtar)
print("kam =",kam)
print("jam =",jam)




