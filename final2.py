import pymysql
import re

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

def ask_question():
    user_input = input("Ask a question (or 'exit' to quit): ")
    return user_input.lower()

def main():
    table_name = "jew"

    # Get all column names of the table
    all_column_names = get_column_names(table_name)

    while True:
        user_input = ask_question()

        if user_input == 'exit':
            print("Goodbye!")
            break

        # Process user input to generate SQL conditions
        conditions = []
        user_input_lower = user_input.lower()

        for column_name in all_column_names:
            if re.search(rf'\b{column_name.lower()}\b', user_input_lower):
                value = input(f"Enter value for {column_name}: ")
                conditions.append(f"{column_name} = '{value}'")

        if conditions:
            conditions_str = " AND ".join(conditions)
            result = search_records(table_name, conditions_str)
            print_results(result, all_column_names)
        else:
            print("Unable to determine the question. Please try again.")

if __name__ == "__main__":
    main()
    connection.close()
