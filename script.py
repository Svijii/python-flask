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

def count_records(table_name, conditions):
    query = f"SELECT COUNT(*) FROM {table_name}"
    if conditions:
        query += f" WHERE {conditions}"
    result = execute_query(query)
    return result[0][0]

def main():
    table_name = "jew"

    # Get all column names of the table
    all_column_names = get_column_names(table_name)
    print("Column Names:", all_column_names)

    while True:
        user_input = input("Ask a question (or 'exit' to quit): ")

        if user_input.lower() == 'exit':
            print("Goodbye!")
            break

        # Separate "count" logic and condition logic
        count_condition = "1"  # Default count condition (count all rows)
        conditions = []

        # Split user input into words
        input_words = user_input.split()

        i = 0
        while i < len(input_words):
            # Check if the word is a recognized column name, a numerical value, or the keyword "count"
            if input_words[i].lower() in all_column_names or input_words[i].isdigit():
                column_name = input_words[i].lower()

                # Check if there is a next word
                if i + 1 < len(input_words):
                    # Assume the next word is the value
                    value = input_words[i + 1]

                    # Check if the next word is the keyword "range"
                    if i + 2 < len(input_words) and input_words[i + 1].lower() == 'range':
                        # Assume the next words are the range values
                        min_value = input_words[i + 2]
                        max_value = input_words[i + 3]

                        # Handle the range condition
                        conditions.append(f"{column_name} BETWEEN {min_value} AND {max_value}")
                        i += 4  # Skip the processed words
                    else:
                        # Handle regular conditions
                        conditions.append(f"{column_name} = '{value}'")
                        i += 2  # Skip the processed words
                else:
                    print(f"Invalid input: Value is missing for column {column_name}.")
                    break
            elif input_words[i].lower() == 'count':
                # Handle the count condition without a specific column name
                count_condition = "1"  # This condition always holds true for counting rows
                i += 1  # Skip the processed word
            else:
                print(f"Invalid input: {input_words[i]} is not a recognized column name.")
                break

        conditions_str = " AND ".join(conditions)
        count = count_records(table_name, conditions_str or count_condition)
        print(f"Number of customers: {count}")

if __name__ == "__main__":
    main()
    connection.close()









