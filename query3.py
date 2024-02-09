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

def get_details(OCCASION):
    query="SELECT DISTINCT OCCASION FROM jewells"
    return execute_query(query)

def get_occasions():
    query = "SELECT COUNT(DISTINCT OCCASION) FROM jewells"
    return execute_query(query)


while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break


    keywords = user_input.lower().split()
    if ("count" in keywords or "number" in keywords or 'howmany' in keywords or "how many" in keywords) and any(keyword in keywords for keyword in ["occasion", "brand", "types", "list","brands","type","lists"]):
        occasion_count = get_occasions()
        print("Number of occasions:")
        print(occasion_count[0][0])
    elif "anniversary" in keywords or "wedding" in keywords or "birthday" in keywords or "graduation" in keywords:
        OCCASION_search_result =get_details('occasion')
        print("count of occasion details :")
        print(OCCASION_search_result)
    else:
        print("Invalid query. Please enter a valid query or 'exit' to quit.")




    # Execute the SQL query







