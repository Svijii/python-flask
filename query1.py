import pymysql

# Establish a connection
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="viji@sight",
    database="amitdb"
)

cursor = connection.cursor()

cursor.execute("SELECT * FROM jewells")

results = cursor.fetchall()

for row in results:
    print(row)

# Close the cursor after fetching initial results
cursor.close()
specific_value = 'ring'
specific_value = 'earrings'
specific_value = 'brooch'
specific_value = 'bracelet'
specific_value = 'necklace'

spe_value = 'bulgari'
spe_value = 'cartier'
spe_value = 'Harry winston'
spe_value = 'Tiffany & co'




def generate_sql_query(jewelry_type,brand_column, question):
    question = question.lower()

    if 'jewelry type' in question or 'available' in question or 'jewel' in question or 'jewelry' in question or 'list' in question :
        return f'SELECT DISTINCT {jewelry_type} FROM jewells;'

    elif 'count' in question or 'ring' in question:
        return f"SELECT COUNT(*) FROM jewells WHERE {jewelry_type_column} = '{specific_value}';"

    elif 'average' in question or 'bulgari' in question:
        return f"SELECT AVG({brand_column}) FROM jewells WHERE {brand_column} = '{spe_value}';"


    else:
        return "I'm sorry, I don't have information on that type of query."

jewelry_type_column = 'jewelry_type'
brand_column = 'brand'

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break

    # Re-establish the cursor for the new query
    cursor = connection.cursor()

    # Generate SQL Query
    sql_query = generate_sql_query(jewelry_type_column,brand_column, user_input)
    print("Generated SQL Query:", sql_query)

    # Execute the SQL query
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
