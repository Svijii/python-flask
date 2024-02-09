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
def search_details(JEWELRY_TYPE):
    query = "SELECT COUNT(DISTINCT JEWELRY_TYPE) FROM JEWELRY_TYPE"
    return execute_query(query)

def search_jewels_by_attributes(JEWELRY_TYPE, MATERIAL=None, GEMESTONE=None, DESIGNER=None, PRICE=None, WIDTH=None, HEIGHT=None, WEIGHT=None, CLASP_TYPE=None, CHAIN_TYPE=None, SETTING_TYPE=None, RING_SIZE=None, EARRING_BACK_TYPE=None, NECKLACE_LENGTH=None, BRACELET_STYLE=None, ENGRAVING=None, BIRTHSTONE=None, OCCASION=None, BRAND=None):
    conditions = [f"JEWELRY_TYPE = '{JEWELRY_TYPE}'"]


    if OCCASION:
        conditions.append(f"occasion = '{OCCASION}'")
    if BRAND:
        conditions.append(f"brand = '{BRAND}'")
    # Add more conditions for other attributes...

    query = f"SELECT * FROM jewells WHERE {' AND '.join(conditions)}"
    return execute_query(query)

# Example usage inside the loop
while True:
    user_input = input("Enter your query (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    result = search_jewels_by_attributes('ring','brooch','necklace''bracelet','earrings', OCCASION='BIRTHDAY', PRICE='<1000')
    print(result)
