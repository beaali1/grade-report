import pandas as pd
df = pd.read_csv("nomarat.csv")

print("Miangin-e har dars:")
print(df.groupby("dars")["grade"].mean())
print()
print("kasani ke amar ra oftade and:")
print(df[(df["dars"] == "amar") & (df["grade"] < 10)])
print()
print("Miangin-e har nafar:")
print(df.groupby("name")["grade"].mean())
print()
print("behtarin nomre ha:")
print(df.groupby("name")["grade"].max())
print()
print("kasani ke dar riazi ra > 15 :")
print(df[(df["dars"] == "riazi") & (df["grade"] > 15)])
print()
print("kasani ke dar riazi ra <= 15 :")
print(df[(df["dars"] == "riazi") & (df["grade"] <= 15)])











