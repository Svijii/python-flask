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

# Scenario 4: Searching for Orders by Date Range
def search_orders_by_date_range(start_date, end_date):
    query = f"SELECT * FROM jew WHERE order_date BETWEEN '{start_date}' AND '{end_date}'"
    return execute_query(query)

# Example usage
while True:
    start_date = input("Enter the start date (YYYY-MM-DD): ")
    end_date = input("Enter the end date (YYYY-MM-DD): ")

    # Call the search_orders_by_date_range function with the provided date range
    result = search_orders_by_date_range(start_date, end_date)

    if result and len(result) > 0:
        print("Orders Placed During the Specified Date Range:")
        for row in result:
            print(f"Order ID: {row[14]}")
            print(f"Customer Name: {row[0]}")
            print(f"Order Date: {row[15]}")
            print(f"Product name: {row[5]}")
            print(f"Product category:{row[6]}")
            print(f"Order Status: {row[16]}")
            print(f"Shipping method: {row[17]}")  # Adjust based on your schema

            # Add more details as needed
    else:
        print("No orders found during the specified date range.")

# Close the connection when done
connection.close()


