import pandas as pd

def remove_and_print_row(csv_path, index_to_remove):
    # Read CSV into a DataFrame
    df = pd.read_csv(csv_path)

    # Remove row by index value
    df = df.drop(index_to_remove, axis=0)

    # Resetting the index to avoid gaps in the index
    df = df.reset_index(drop=True)

    # Set options to display all rows and columns
    pd.set_option('display.max_rows', None)
    pd.set_option('display.max_columns', None)

    # Print the updated DataFrame
    print(df)

if __name__ == "__main__":
    csv_file_path = r'C:\Users\SightSpectrum\Desktop/output.csv'
    index_to_remove = 3
    index_to_remove = 3


    remove_and_print_row(csv_file_path, index_to_remove)









