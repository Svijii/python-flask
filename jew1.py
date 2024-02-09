import re
import pymysql

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

# Function to search for product details by name
def search_product_details(product_name):
    query = f"""
        SELECT
            order_id,
            customer_name,
            order_date,
            order_status,
            shipping_method,
            product_name,
            brand,
            price,
            weight,
            height,
            width
        FROM
            jew
        
        WHERE
            LOWER(product_name) LIKE %s;
    """
    params = ('%' + product_name.lower() + '%',)
    return execute_query(query, params)

# Function to extract product name from user input
def extract_product_name(user_input):
    # List of valid product names
    valid_products = ['ring', 'necklace', 'brooch', 'bracelet','earrings']

    # Split the user input into individual words
    words = user_input.split()

    # Check for valid product names
    for i, word in enumerate(words):
        if word.lower() in valid_products:
            return word.lower()

    return None

# Example usage
while True:
    user_input = input("Enter your request (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Extract product name from user input
    product_name = extract_product_name(user_input)

    if product_name:
        # Call the search_product_details function with the extracted product name
        result = search_product_details(product_name)

        if result and len(result) > 0:
            print("Product Details:")
            for row in result:
                # Check if the tuple has at least 15 elements before accessing them

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
            print(f"No details found for the product: {product_name}")
    else:
        print("Invalid product name detected. Please ask about a valid product.")

# Close the connection when done
