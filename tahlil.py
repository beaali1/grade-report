import pandas as pd
df = pd.read_csv("nomarat.csv")
print(df.groupby("dars")["grade"].mean())