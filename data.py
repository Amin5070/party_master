import mysql.connector

# Replace with your database and user information
config = {
    "host": "localhost",
    "user": "Amin5070",
    "password": "Amin@5070",
    "database": "mypartymasterDB",
}

# Establish a connection to the database
conn = mysql.connector.connect(**config)

# Create a cursor to execute SQL queries
cursor = conn.cursor()

# Execute a SELECT query
query = "SELECT * FROM party_master_partymaster;"
cursor.execute(query)

# Fetch and display the results
for row in cursor.fetchall():
    print(row)

# Close the cursor and connection
cursor.close()
conn.close()
