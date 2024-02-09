import pandas as pd
filepath =r"C:\Users\SightSpectrum\Desktop\data - Copy.csv"
df = pd.read_csv(filepath)
#print(df.head)
df.fillna(130, inplace = True)
print(df.to_string())
import numpy as np
#print("------Raw Data------")
#df = pd.read_csv(r'C:\Users\SSLTP11158\PycharmProjects\pythonProject\portal\venv\sample2.csv')
#print(df.head)
#df4 = df.fillna({ 'calories' : '50.7',})
#print(df4)

#df4.to_csv(r'C:\Users\SSLTP11158\PycharmProjects\pythonProject\portal\venv\sample_cleaned.csv', encoding = 'utf-8' , index = False)




#print(df.shape)
#print(df.isnull().sum())
#print(df.dropna(inplace=True))
#df.drop_duplicates(inplace = True)

#print(df.to_string())
#df.fillna(130, inplace = True)
#print(df.to_string())

