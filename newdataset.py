import pymysql

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="viji@sight",
    database="amitdb"
)

def execute_query(query, params=None):
    cursor = connection.cursor()
    try:
        if params:
            cursor.execute(query, params)
        else:
            cursor.execute(query)
        result = cursor.fetchall()
        return result
    except pymysql.Error as e:
        print(f"Error executing SQL query: {e}")
    finally:
        cursor.close()

def get_column_names(table_name):
    query = f"SHOW COLUMNS FROM {table_name}"
    result = execute_query(query)
    return [column[0] for column in result]

def get_column_values(table_name):
    query = f"SHOW COLUMNS FROM {table_name}"
    result = execute_query(query)
    return [column[0] for column in result]

def search_records(table_name, conditions):
    query = f"SELECT * FROM {table_name} WHERE {conditions}"
    return execute_query(query)

def find_date_column(table_name, column_names):
    # Look for common date-related column names
    date_keywords = ['date', 'time', 'day', 'month', 'year']
    for column in column_names:
        if any(keyword in column.lower() for keyword in date_keywords):
            return column
    return None

def print_results(result, column_names, column_values):
    if result:
        print("Search Results:")
        for row in result:
            for i, value in enumerate(row):
                print(f"{column_names[i]}: {value}")
            print("\n")
    else:
        print("No results found.")

def ask_question(all_column_names, column_values):
    user_input = input("Enter conditions (or 'exit' to quit): ")
    return user_input.lower()

def main():
    table_name = "jew"

    # Get all column names and values of the table
    all_column_names = get_column_names(table_name)
    all_column_values = get_column_values(table_name)
    columns = get_column_names(table_name)
    print("Column Names:", columns)

    while True:
        user_input = ask_question(all_column_names, all_column_values)

        if user_input == 'exit':
            print("Goodbye!")
            break

        # Process user input to generate SQL conditions
        conditions = []

        # Split user input into words
        input_words = user_input.split()

        column_name = None
        i = 0
        while i < len(input_words):
            # Check if the word is a known column name or value
            if input_words[i].lower() in all_column_names or input_words[i].lower() in all_column_values:
                column_name = input_words[i].lower()

                if column_name == 'price' and i + 3 < len(input_words) and input_words[i + 1].lower() == 'range':
                    # Handle the price range condition
                    min_price = input_words[i + 2]
                    max_price = input_words[i + 4]  # Skip the 'to' keyword
                    conditions.append(f"{column_name} BETWEEN {min_price} AND {max_price}")
                    i += 5  # Skip the processed words
                elif column_name == 'daterange' and i + 3 < len(input_words) and input_words[i + 2].lower() == 'to':
                    # Handle the date range condition
                    start_date = input_words[i + 1]
                    end_date = input_words[i + 3]
                    # Automatically find the date column
                    date_column = find_date_column(table_name, all_column_names)
                    if date_column:
                        conditions.append(f"{date_column} BETWEEN '{start_date}' AND '{end_date}'")
                    else:
                        print("Invalid input: Date column not found.")
                        break
                    i += 4  # Skip the processed words
                else:
                    # Handle regular conditions
                    value = input_words[i + 1]
                    conditions.append(f"{column_name} = '{value}'")
                    i += 2  # Skip the processed words
            else:
                print(f"Invalid input: {input_words[i]} is not a recognized column name or value.")
                break

        if conditions:
            conditions_str = " AND ".join(conditions)
            result = search_records(table_name, conditions_str)
            print_results(result, all_column_names, all_column_values)
        else:
            print("No conditions specified. Please try again.")

if __name__ == "__main__":
    main()
    connection.close()
