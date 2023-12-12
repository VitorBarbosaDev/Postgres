import os
from dotenv import load_dotenv
import psycopg2

# Load environment variables from .env file
load_dotenv()

# Retrieve environment variables
db_name = os.getenv('DB_NAME')
db_user = os.getenv('DB_USER')
db_pass = os.getenv('DB_PASS')
db_host = os.getenv('DB_HOST')
db_port = os.getenv('DB_PORT')

# connect to "chinook" database
connection = psycopg2.connect(database=db_name, user=db_user, password=db_pass, host=db_host, port=db_port)

# build a cursor object of database
cursor = connection.cursor()

#Query 1 - select all records from the "Artist" table
cursor.execute('SELECT * FROM "Artist"')

# fetch the results (mutiple)
results = cursor.fetchall()

# close the connection
connection.close()

# print the results
for result in results:
    print(result)