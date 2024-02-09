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

def search_records(table_name, date_columns, start_date, end_date):
    conditions = []
    for column in date_columns:
        conditions.append(f"{column} BETWEEN '{start_date}' AND '{end_date}'")

    conditions_str = " OR ".join(conditions)
    if conditions_str:
        query = f"SELECT * FROM {table_name} WHERE {conditions_str}"
        return execute_query(query)
    else:
        print("No conditions specified. Please try again.")
        return None

def print_results(result, column_names):
    if result:
        print("Search Results:")
        for row in result:
            for i, value in enumerate(row):
                print(f"{column_names[i]}: {value}")
            print("\n")
    else:
        print("No results found.")

def ask_question():
    date_range = input("Enter date range (or 'exit' to quit): ")
    return date_range.lower()

def get_date_columns(table_name):
    query = f"SHOW COLUMNS FROM {table_name} WHERE Type LIKE 'date%'"
    result = execute_query(query)
    return [column[0] for column in result]

def parse_date_range(date_range):
    try:
        start_date, end_date = map(str.strip, date_range.split(' to '))
        return start_date, end_date
    except ValueError:
        return None, None

def main():
    table_name = "jwdb"  # Replace with your actual table name

    # Get all date columns of the table
    date_columns = get_date_columns(table_name)

    while True:
        user_input = ask_question()

        if user_input == 'exit':
            print("Goodbye!")
            break

        # Process user input to generate dynamic SQL conditions
        start_date, end_date = parse_date_range(user_input)

        if start_date is not None and end_date is not None:
            result = search_records(table_name, date_columns, start_date, end_date)
            print_results(result, date_columns)
        else:
            print("Invalid date range format. Please try again.")

if __name__ == "__main__":
    main()
    connection.close()

