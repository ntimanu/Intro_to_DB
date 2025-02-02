import mysql.connector
from mysql.connector import Error

try:
    # Establish connection to MySQL server (Change username & password as needed)
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="root123"
    )

    # Create a cursor object to execute SQL statements
    mycursor = mydb.cursor()

    # Create the database if it does not exist
    mycursor.execute("CREATE DATABASE IF NOT EXISTS alx_book_store")

    print("Database 'alx_book_store' created successfully!")

except Error as e:
    print(f"Error: {e}")

finally:
    # Close the cursor and database connection
    if 'mycursor' in locals():
        mycursor.close()
    if 'mydb' in locals() and mydb.is_connected():
        mydb.close()
        print("Database connection closed.")