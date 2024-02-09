import pandas as pd
df =pd.read_csv(r'C:\Users\SightSpectrum\Desktop\jewellary_dataset.csv')
print(df)
print(df.shape)
# Drop duplicates
df = df.drop_duplicates()
print(df)
print(df.shape)
# Drop rows with missing values
df = df.dropna()
print(df)
print(df.shape)
df.to_csv(r'C:\Users\SightSpectrum\Desktop\jewellary_dataset_Final.csv', encoding = 'utf-8' , index = False)
#print(df)
#print(df.shape)
#df.fillna(130, inplace = True)
#print(df.to_string())
