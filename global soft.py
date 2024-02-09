import fitz  # PyMuPDF
import csv

def convert_pdf_to_csv(pdf_path, csv_path):
    doc = fitz.open(pdf_path)
    text = ""

    for page_num in range(doc.page_count):
        page = doc[page_num]
        text += page.get_text()

    # Split the text into lines and write to CSV
    lines = text.split('\n')
    with open(csv_path, 'w', newline='', encoding='utf-8') as csv_file:
        csv_writer = csv.writer(csv_file)
        for line in lines:
            csv_writer.writerow([line])

if __name__ == "__main__":
    pdf_file_path = r'C:\Users\SightSpectrum\Desktop\Global.pdf'
    csv_output_path = import pandas as pd


    convert_pdf_to_csv(pdf_file_path, csv_output_path)
