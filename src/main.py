import pandas as pd

df = pd.read_csv("data/owid-co2-data.csv")

print("Dataset loaded successfully!")
print(df.head())
print(df.columns)
