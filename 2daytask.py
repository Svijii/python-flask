import pdfplumber
import csv

def extract_table_data(pdf_path):
    with pdfplumber.open(pdf_path) as pdf:
        # Assuming the table is on the first page
        first_page = pdf.pages[0]

        # Define the coordinates of the table (adjust these values based on your PDF)
        table_bbox = (100, 200, 300, 400)  # Replace with actual coordinates

        # Extract the table using the defined coordinates
        table = first_page.crop(bbox=table_bbox).extract_table()

        return table

def write_to_csv(table, csv_path):
    with open(csv_path, 'w', newline='') as csvfile:
        csv.writer(csvfile).writerows(table)

if __name__ == "__main__":
    pdf_path = r'C:\Users\SightSpectrum\Desktop\Global.pdf'
    csv_path = r'C:\Users\SightSpectrum\Desktop\fi.csv'

    table = extract_table_data(pdf_path)

    if table:
        write_to_csv(table, csv_path)
        print("CSV file created successfully.")
    else:
        print("Table not found. Please adjust coordinates.")







