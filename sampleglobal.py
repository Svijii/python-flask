import pandas as pd
import pdfplumber
import re
from tabulate import tabulate

pdf_path = r'C:\Users\SightSpectrum\Desktop\Global.pdf'

with pdfplumber.open(pdf_path) as pdf:
    text_data = ''
    for page in pdf.pages:
        text_data += page.extract_text()

lines = text_data.split('\n')
data_list = []

# Process header line
header = lines[1].split('\t')
data_list.append(header)

# Process data lines
for line in lines[1:]:
    columns = line.split('\t')
    data_list.append(columns)

# Create DataFrame
df = pd.DataFrame(data_list[1:], columns=data_list[0])

# Remove unwanted characters from column names
df.columns = [re.sub(r'[^\w\s]', '', col) for col in df.columns]

# Remove the first three rows
df = df.iloc[2:]

# Display DataFrame in Excel-like format
print(tabulate(df, headers='keys', tablefmt='fancy_grid', showindex=False))





















