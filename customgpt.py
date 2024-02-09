import pandas as pd
filepath=r"C:\Users\SightSpectrum\Desktop\Jewellary_Dataset_Final.csv"
dataset=pd.read_csv(filepath)
print(dataset.to_string())
