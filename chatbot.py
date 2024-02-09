import pymysql

# Establish a connection to the database
connection = pymysql.connect(
    host="localhost",
    user="root",
    password="viji@sight",
    database="amitdb"
)

# Create a cursor to execute SQL queries
cursor = connection.cursor()

# Example query to retrieve all items from the "jewells" table
query = "SELECT * FROM jewells"
cursor.execute(query)

# Fetch all the results
results = cursor.fetchall()

# Print each row
for row in results:
    print(row)

# Close the cursor and connection
cursor.close()
connection.close()
