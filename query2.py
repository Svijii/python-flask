import pymysql
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
os = 'anniversary'
os = 'wedding'
os = 'birthday'
os = 'graduation'
def query(occasion,question):
    question = question.lower()
    occasions = ['wedding', 'anniversary', 'birthday', 'graduation']
    if any(occasion in question for occasion in occasions) or 'how' in question or 'list' in question or 'available' in question:
        occasion_conditions = ', '.join(f"'{occasion}'" for occasion in occasions)
        return f"SELECT occasion, COUNT(*) as occasion_count FROM jewells WHERE occasion IN ({occasion_conditions}) GROUP BY occasion;"





     #return "SELECT item, COUNT(*) as item_count FROM jewells GROUP BY item;"

    #if 'occasion'in question or 'wedding' in question or 'anniversary' in question or 'birthday' in question or 'graduation' in question or 'how'in question:
       # return "SELECT occasion, COUNT(*) as occasion_count FROM jewells WHERE occasion IN ('graduation', 'wedding', 'birthday') GROUP BY occasion;"

        #return f"SELECT COUNT(*) FROM jewells WHERE {occasion} = '{os}';"
    #elif 'birthday' in question or 'total'in question:
        #return f"SELECT COUNT(*) FROM jewells WHERE {occasion} =' {occasion}';"


    else:
         return "I'm sorry, I don't have information on that type of query."

occasion_column = 'occasion'

while True:
    user_input = input("You: ")
    if user_input.lower() == 'exit':
        print("Goodbye!")
        break
         # Re-establish the cursor for the new query
    cursor = connection.cursor()

    # Generate SQL Query
    sql_query = query(occasion_column, user_input)
    #print("Generated SQL Query:", sql_query)

    # Execute the SQL query
    try:
        cursor.execute(sql_query)
        results = cursor.fetchall()
         # Print the results
        for row in results:
            #print(row)
            if row[0] == 'graduation':
               print(f"Count of 'graduation': {row[1]}")
            #elif row[0] =='wedding':
               #print(f"Count of 'wedding': {row[1]}")
            #elif row[0] == 'anniversary':
               #print(f"Count of 'anniversary': {row[1]}")
            #elif row[0] == 'birthday':
             #print(f"Count of 'birthday': {row[1]}")



    except pymysql.Error as e:
        print(f"Error executing SQL query: {e}")

    finally:
        # Close the cursor after each query
        cursor.close()

# Close the connection when done
connection.close()












