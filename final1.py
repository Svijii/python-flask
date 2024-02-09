
import pymysql
import phonenumbers
import re

# Connect to the database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="viji@sight",
    database="amitdb"
)

# Function to execute SQL queries
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
def extract_product_name(user_input):
    # List of valid product names
    valid_products = ['yellow', 'rose', 'white',]

    # Split the user input into individual words
    words = user_input.split()

    # Check for valid product names
    for i, word in enumerate(words):
        if word.lower() in valid_products:
            return word.lower()

    return None

def search_order_by_product_id(product_id):
    query = f"SELECT * FROM jew WHERE product_id = '{product_id}'"
    return execute_query(query)
def search_order_by_color(color):
    query = f"SELECT * FROM jew WHERE color = '{color}'"
    return execute_query(query)
def search_order_by_customer_name(customer_name):
    query = f"SELECT * FROM jew WHERE customer_name = '{customer_name}'"
    return execute_query(query)
def search_order_by_email(email):
    query = f"SELECT * FROM jew WHERE email='{email}'"
    return execute_query(query)
def search_order_by_product_name(product_name):
    query = f"SELECT * FROM jew WHERE product_name='{product_name}'"
    return execute_query(query)
def search_orders_by_date_range(start_date, end_date):
    query = f"SELECT * FROM jew WHERE order_date BETWEEN '{start_date}' AND '{end_date}'"
    return execute_query(query)

def search_order_by_order_id(order_id):
    query = f"SELECT * FROM jew WHERE order_id ='{order_id}'"
    return execute_query(query)




valid_product_names = ["ring", "brooch", "necklace", "earrings", "bracelet"]
# Example usage
while True:
    user_input = input("Enter the product ID or color to search (or 'exit' to quit): ")

    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
    #result = None

    # Check if the input is a product ID
    if re.match(r'\d+', user_input):
        result = search_order_by_product_id(user_input)

        if result:
            print("product  Details:")
            for row in result:
                # Print details based on the result
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
        else:
            print(f"No product order found with ID: {user_input}")

    else:
        # Extract color from the input
        color_match = re.search(r'\b(?:yellow|rose|white)\b', user_input, flags=re.IGNORECASE)

        if color_match:
            color = color_match.group(0).lower()
            result = search_order_by_color(color)

            if result:
                print("Product Details:")
                for row in result:
                    # Print details based on the result
                    print(f"Customer name: {row[0]}")  # Index 1 corresponds to customer_name
                    print(f"Order date: {row[15]}")  # Index 2 corresponds to order_date
                    print(f"Order status: {row[16]}")  # Index 3 corresponds to order_status
                    print(f"Shipping method: {row[17]}")  # Index 4 corresponds to shipping_method
                    print(f"Product name: {row[5]}")
                    print(f"Brand: {row[6]}")
                    print(f"Price: {row[7]}")
                    print(f"Weight: {row[8]}")
                    print(f"Height: {row[9]}")
                    print(f"Width: {row[10]}")
                    print(f"color : {row[13]}")

            else:
                print(f"No details found for the color: {color}")
        else:
            # Check if the input is a date in the format MM/DD/YYYY
            date_match = re.match(r'(\d{1,2}/\d{1,2}/\d{4})', user_input)

            if date_match:
                start_date_str = date_match.group(1)
                start_date = datetime.strptime(start_date_str, '%m/%d/%Y')

                # Suggest an end date
                end_date_input = input(f"Suggested end date (format: MM/DD/YYYY) for {start_date_str}: ")
                end_date_match = re.match(r'(\d{1,2}/\d{1,2}/\d{4})', end_date_input)

                if end_date_match:
                    end_date_str = end_date_match.group(1)
                    end_date = datetime.strptime(end_date_str, '%m/%d/%Y')

                    # Call the function with the date range
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
                    else:
                        print("No orders found during the specified date range.")
                else:
                    print("Invalid end date format. Please use the format MM/DD/YYYY.")
    # Call the search_orders_by_date_range function with the provided date range
                #result = search_orders_by_date_range(start_date, end_date)

                 #result = search_orders_by_date_range(start_date, end_date)

                if result and len(result) > 0:
                    print("Orders Placed During the Specified Date Range:")
                    for row in result:
                        print(f"Order ID: {row[14]}")
                        print(f"Customer Name: {row[0]}")
                        print(f"Order Date: {row[15]}")
                        print(f"Product name: {row[5]}")
                        print(f"Product category:{row[6]}")
                        print(f"Order Status: {row[16]}")
                        print(f"Shipping method: {row[17]}")
                        # Add more details as needed
                else:
                    print("No orders found during the specified date range")


    # If not a product ID or color, assume it's an order ID
    if user_input.lower() in valid_product_names:
        result_product_name = search_order_by_product_name(user_input)

        if result_product_name:
            print("Product Details:")
            for row in result_product_name:
                # Print details based on the result
                print(f"Order ID: {row[0]}")  # Index 0 corresponds to order_id
                print(f"Customer name: {row[1]}")  # Index 1 corresponds to customer_name
                print(f"Order date: {row[2]}")  # Index 2 corresponds to order_date
                print(f"Order status: {row[3]}")  # Index 3 corresponds to order_status
                print(f"Shipping method: {row[4]}")  # Index 4 corresponds to shipping_method
                print(f"Product name: {row[5]}")
                print(f"Brand: {row[6]}")
                print(f"Price: {row[7]}")
                print(f"Weight: {row[8]}")
                print(f"Height: {row[9]}")
                print(f"Width: {row[10]}")
        else:
            print(f"No details found for the product: {user_input}")
    else:
        print("Invalid product name detected. Please ask about a valid product.")

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
connection.close()
