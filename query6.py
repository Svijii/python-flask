import pymysql

def execute_query(query):
    connection = pymysql.connect(
        host="localhost",
        user="root",
        password="viji@sight",
        database="amitdb"
    )
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()
        connection.close()

def chatbot_query(input_text):
    # Split the input text into keywords
    keywords = input_text.lower().split()

    # Check for specific keywords and generate appropriate queries
    if "jewelry_type" in keywords:
        return search_jewels_by_jewelry_type('gold')
    elif "gold" in keywords:
        return search_jewels_by_attributes('gold', OCCASION='BIRTHDAY', PRICE='<1000')
    else:
        return "I'm sorry, I don't have information on that type of query."

def search_jewels_by_jewelry_type(jewelry_type):
    query = f"SELECT * FROM jewells WHERE JEWELRY_TYPE = '{jewelry_type}'"
    return execute_query(query)

def search_jewels_by_attributes(jewelry_type, OCCASION=None, PRICE=None):
    conditions = [f"JEWELRY_TYPE = '{jewelry_type}'"]

    if OCCASION:
        conditions.append(f"occasion = '{OCCASION}'")
    if PRICE:
        conditions.append(f"price {PRICE}")
    # Add more conditions for other attributes...

    query = f"SELECT * FROM jewells WHERE {' AND '.join(conditions)}"
    return execute_query(query)

# Example usage:
