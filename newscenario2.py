import pymysql

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="viji@sight",
    database="amitdb"
)

# Function to execute SQL queries
def execute_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    except pymysql.Error as e:
        print(f"Error executing SQL query: {e}")
    finally:
        cursor.close()

# Scenario 1: Searching for Orders by Order ID
def search_order_by_product_id(product_id):
    query = f"SELECT * FROM jew WHERE product_id = '{product_id}'"
    return execute_query(query)

# Example usage
while True:
    user_input = input("Enter the product ID to search (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Call the search_order_by_order_id function with the provided order ID
    result = search_order_by_product_id(user_input)

    if result:
        print("Order Details:")
        for row in result:
            print(f"product_id: {row[4]}")
            print(f"product_name:{row[5]}")
            print(f"category:{row[6]}")
            print(f"price:{row[7]}")
            print(f"weight:{row[8]}")
            print(f"customer_name:{row[0]}")
            print(f"gender:{row[1]}")
            print(f"email:{row[2]}")
            print(f"phone_number:{row[3]}")
            print(f"Height:{row[9]}")
            print(f"width:{row[10]}")
            print(f"brand:{row[11]}")
            print(f"designer:{row[12]}")
            print(f"color:{row[13]}")
            print(f"order_id:{row[14]}")
            print(f"order_date:{row[15]}")
            print(f"order_status:{row[16]}")
            print(f"shipping_method:{row[17]}")
            print(f"availability:{row[18]}")
            print(f"description:{row[19]}")

            # Add more details as needed

    else:
        print(f"No order found with ID: {user_input}")

# Close the connection when done
connection.close()



