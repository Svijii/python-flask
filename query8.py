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

def get_material_details():
    query = "SELECT DISTINCT MATERIAL FROM jewells"
    return execute_query(query)
def get_details_for_material(material):
    query = f"SELECT * FROM jewells WHERE MATERIAL = '{material}'"
    return execute_query(query)
def count_materials():
    query = "SELECT COUNT(DISTINCT MATERIAL) FROM MATERIAL"
    return execute_query(query)
while True:
    user_input = input("Enter your query (or 'exit' to quit): ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    keywords = user_input.lower().split()
    if ("count" in keywords or "number" in keywords or 'howmany' in keywords or "how many" in keywords) and any(keyword in keywords for keyword in ["material", "brand", "types", "list","brands","type","lists"]):
        material_count = count_materials()
        print("Number of materials:")
        print(material_count[0][0])
    elif "gold" in keywords:
        MATERIAL_search_result =get_details_for_material('gold')
        print("jewelry types from gold :")
        print(MATERIAL_search_result)
    elif "silver" in keywords:
        MATERIAL_search_result =get_details_for_material('silver')
        print("jewelry types from silver :")
        print(MATERIAL_search_result)
    elif "pearl" in keywords:
        MATERIAL_search_result =get_details_for_material('pearl')
        print("jewelry types from pearl :")
        print(MATERIAL_search_result)
    elif "diamond" in keywords:
        MATERIAL_search_result =get_details_for_material('diamond')
        print("jewels types from diamond :")
        print(MATERIAL_search_result)
    elif "platinum" in keywords:
        MATERIAL_search_result =get_details_for_material('platinum')
        print("jewelry types from platinum :")
        print(MATERIAL_search_result)
    elif any(keyword in keywords for keyword in ["material", "brands","brand" ,"types","type", "lists","list"]):
        material_details = get_material_details()
        print("Material details:")
        print(material_details)
    else:
        print("Invalid query. Please enter a valid query or 'exit' to quit.")
