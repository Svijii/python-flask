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

def get_table_info(table_name):
    # Retrieve information about the columns in the table
    query = f"DESCRIBE {table_name}"
    result = execute_query(query)
    return [column[0] for column in result]

def search_records(table_name, conditions):
    query = f"SELECT * FROM {table_name} WHERE {conditions}"
    return execute_query(query)

def print_results(result, column_names):
    if result:
        print("Search Results:")
        for row in result:
            for i, value in enumerate(row):
                print(f"{column_names[i]}: {value}")
            print("\n")
    else:
        print("No results found.")

def ask_question(table_name):
    user_input = input("Enter conditions (or 'exit' to quit): ")
    return user_input.lower()

def find_date_column(table_name, column_names):
    # Look for common date-related column names
    date_keywords = ['date', 'time', 'day', 'month', 'year']
    for column in column_names:
        if any(keyword in column.lower() for keyword in date_keywords):
            return column
    return None

def main():
    table_name = "jew"  # Replace with your actual table name

    # Get all column names in the table
    all_column_names = get_table_info(table_name)

    while True:
        user_input = ask_question(table_name)

        if user_input == 'exit':
            print("Goodbye!")
            break

        # Process user input to generate SQL conditions
        conditions = []

        # Split user input into words
        input_words = user_input.split()

        i = 0
        while i < len(input_words):
            term = input_words[i].lower()

            if term == 'daterange' and i + 3 < len(input_words) and input_words[i + 2].lower() == 'to':
                start_date = input_words[i + 1]
                end_date = input_words[i + 3]

                # Automatically find the date column
                date_column = find_date_column(table_name, all_column_names)
                if date_column:
                    conditions.append(f"{date_column} BETWEEN '{start_date}' AND '{end_date}'")
                else:
                    print("Unable to determine the date column. Please specify.")
                    break

                i += 4  # Skip the processed words
            else:
                # Handle other terms or use a default column name
                default_column = "default_column"
                value = input_words[i]
                conditions.append(f"{default_column} = '{value}'")
                i += 1  # Skip the processed word

        if conditions:
            conditions_str = " AND ".join(conditions)
            column_names = all_column_names if all_column_names else ["*"]
            result = search_records(table_name, conditions_str)
            print_results(result, column_names)
        else:
            print("No conditions specified. Please try again.")

if __name__ == "__main__":
    main()
    connection.close()
