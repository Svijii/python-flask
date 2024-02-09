import pandas as pd

filepath = r"C:\Users\SightSpectrum\Desktop\Jewellary _Dataset_Final.csv"  # Replace YourFile.csv with the actual CSV file name
dataset = pd.read_csv(filepath)

# Print the entire dataset as a string
#print(dataset.to_string())
#print(dataset.loc[1])
#print(pd.options.display.max_rows)
#print(dataset.head(20))
print(dataset.info())
