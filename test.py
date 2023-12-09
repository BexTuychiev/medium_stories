import mysql.connector

# Database connection details
HOST = "172.17.0.2"  # Replace with container IP if running remotely
PORT = 3306  # Default MySQL port
USER = "root"  # Replace with your username
PASSWORD = "strong_password"  # Replace with your password
DATABASE = "products"  # Replace with your database name

# Connect to the database
try:
    connection = mysql.connector.connect(
        host=HOST,
        port=PORT,
        user=USER,
        password=PASSWORD,
        database=DATABASE,
    )
    print("Connected to MySQL database successfully!")

    # Create a cursor object
    cursor = connection.cursor()

    # Execute a sample query
    cursor.execute("SELECT 'hello world!'")

    # Fetch and print the results
    results = cursor.fetchall()
    for row in results:
        print(row)

except mysql.connector.Error as error:
    print(f"Error: {error}")

finally:
    # Close the cursor and connection
    if connection.is_connected():
        cursor.close()
        connection.close()
        print("Connection closed.")