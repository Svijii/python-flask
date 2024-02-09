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

# Function to search orders by order ID
def search_order_by_order_id(order_id):
    query = f"SELECT * FROM jew WHERE order_id = '{order_id}'"
    return execute_query(query)

# Function to search orders by date range
def search_orders_by_date_range(start_date, end_date):
    query = f"SELECT * FROM jew WHERE order_date BETWEEN '{start_date}' AND '{end_date}'"
    return execute_query(query)

# Example usage
while True:
    user_input = input("Enter the start date (MM/DD/YYYY) or order ID (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Check if the input is a numeric value (assumed to be an order ID)
    if user_input.isdigit():
        result_order_id = search_order_by_order_id(user_input)

        if result_order_id:
            print("Order Details:")
            for row in result_order_id:
                print(f"product_id: {row[4]}")
                print(f"product name:{row[5]}")
                print(f"price:{row[7]}")
                print(f"weight:{row[8]}")

                # Add more details as needed
        else:
            print(f"No order found with ID: {user_input}")

    else:
        # Assume the input is a start date; ask for the end date
        start_date = user_input
        end_date = input("Enter the end date (MM/DD/YYYY): ")

        # Call the search_orders_by_date_range function with the provided date range
        result_date_range = search_orders_by_date_range(start_date, end_date)

        if result_date_range and len(result_date_range) > 0:
            print("Orders Placed During the Specified Date Range:")
            for row in result_date_range:
                print(f"Order ID: {row[14]}")
                print(f"Customer Name: {row[0]}")
                print(f"Order Date: {row[15]}")
                print(f"Product name: {row[5]}")
                print(f"Product category: {row[6]}")
                print(f"Order Status: {row[16]}")
                print(f"Shipping method: {row[17]}")  # Adjust based on your schema

                # Add more details as needed
        else:
            print("No orders found during the specified date range.")

# Close the connection when done
connection.close()

