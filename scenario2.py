import pymysql
import phonenumbers

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

# Function to validate and format phone numbers
# Function to validate and format phone numbers
#import phonenumbers




# Scenario 1: Searching for Orders by Customer Information
def search_order_by_customer_name(customer_name):
    query = f"SELECT * FROM jew WHERE customer_name = '{customer_name}'"
    return execute_query(query)

def search_order_by_email(email):
    query = f"SELECT * FROM jew WHERE email = '{email}'"
    return execute_query(query)

def search_order_by_phone_number(phone_number):
    query = f"SELECT * FROM jew WHERE phone_number = '{phone_number}'"
    return execute_query(query)

# Example usage
while True:
    user_input = input("Enter the customer information to search (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Determine the type of search based on user input
    result = None

    # Check for email
    email_result = search_order_by_email(user_input)
    if email_result:
        result = email_result
    else:
        result = search_order_by_customer_name(user_input)

    if result:
        print("Customers information:")
        for row in result:
            print(f"customer_name:{row[0]}")
            print(f"gender:{row[1]}")
            print(f"email:{row[2]}")

            print(f"product_name: {row[5]}")
            print(f"phone_number: {row[3]}")
            print(f"price: {row[7]}")
            print(f"weight: {row[8]}")

            # Add more details as needed

    else:
        print(f"No order found with customer information: {user_input}")

# Close the connection when done
connection.close()


