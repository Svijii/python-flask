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

def search_orders_by_column_value(table_name, column_name, column_value):
    query = f"SELECT * FROM {table_name} WHERE {column_name} = %s"
    return execute_query(query, (column_value,))

def get_all_products(table_name):
    query = f"SELECT DISTINCT {column_name} FROM {table_name}"
    return execute_query(query)
def fetch_column_values(table_name, column_name):
    query = f"SELECT {column_name} FROM {table_name}"
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
    table_name = "jw"
    all_column_names = get_column_names(table_name)

    columns = get_column_names(table_name)
    print("Column Names:", columns)

    while True:
        user_input = ask_question()

        if user_input == 'exit':
            print("Goodbye!")
            break

        found_column = None
        for column_name in all_column_names:
            if column_name.lower() in user_input.lower():
                found_column = column_name
                break

        if found_column:
            # If the user input matches a column name, search for specific details
            column_value = input(f"Enter {found_column} for the product: ")
            result = search_orders_by_column_value(table_name, found_column, column_value)
            print_results(result, all_column_names)
            found_column = None
        for column_name in all_column_names:
            if re.search(rf'\b{column_name.lower()}\b', user_input.lower()):
                found_column = column_name
                break

        if found_column:
            column_values = fetch_column_values(table_name, found_column)
            print_results(column_values, [found_column])
        #elif "products" in user_input.lower():
            # User is asking about products
           # products = get_all_products(table_name)
            #print_results(products, [column_values])
        else:
            print("Unable to determine the question. Please try again.")

if __name__ == "__main__":
    main()
    connection.close()
