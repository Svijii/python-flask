import pandas as pd
filepath = r"C:

df = pd.read_csv('data.csv')

new_df = df.dropna()

print(new_df.to_string())
