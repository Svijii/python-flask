import pymysql

connection = pymysql.connect(
    host="localhost",
    user="root",
    password="viji@sight",
    database="amitdb"
)

def execute_query(query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        result = cursor.fetchall()
        return result
    finally:
        cursor.close()

def search_jewels_by_JEWELRY_TYPE(JEWELRY_TYPE):
    query = f"SELECT * FROM jewells WHERE JEWELRY_TYPE = '{JEWELRY_TYPE}'"
    return execute_query(query)

def search_jewels_by_attributes(JEWELRY_TYPE, OCCASION=None, BRAND=None, PRICE=None):
    conditions = [f"JEWELRY_TYPE = '{JEWELRY_TYPE}'"]

    if OCCASION:
        conditions.append(f"occasion = '{OCCASION}'")
    if BRAND:
        conditions.append(f"brand = '{BRAND}'")
    if PRICE:
        conditions.append(f"PRICE < {PRICE}")

    query = f"SELECT * FROM jewells WHERE {' AND '.join(conditions)}"
    return execute_query(query)

while True:
    user_input = input("Enter your query (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    keywords = user_input.lower().split()
    JEWELRY_TYPE_search_result = search_jewels_by_JEWELRY_TYPE('ring')
    print("jewels types from ring:")
    print(JEWELRY_TYPE_search_result)

    attributes_search_result = search_jewels_by_attributes('ring', OCCASION='BIRTHDAY', BRAND='BULGARI', PRICE='1000')
    print(f"Ring from jewells with OCCASION: BIRTHDAY, BRAND: BULGARI, and a price below 1000:")
    print(attributes_search_result)

# Don't forget to close the connection when done
connection.close()

