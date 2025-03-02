import mysql.connector
import pandas as pd

# Replace these with your database details
username = 'root'              # Your MySQL username (default for XAMPP is 'root')
password = ''                  # Your MySQL password (default for XAMPP is '' (empty))
database_name = 'sample'       # Your database name
host = '127.0.0.1'             # Default host for local MySQL server
port = 3306                    # Default MySQL port (as integer)

# Establish the connection using mysql-connector
conn = mysql.connector.connect(
    host=host,
    user=username,
    password=password,
    database=database_name,
    port=port
)

print("Connection to MySQL database established successfully!")

# Example query
query = "SELECT * FROM users;"  # Replace with your table name

# Execute the query and load data into a Pandas DataFrame
df = pd.read_sql(query, conn)

# Check if DataFrame is empty
if df.empty:
    print("No data found in the table.")
else:
    print("Data fetched successfully!")
    print(df.head())  # Display the first few rows of the DataFrame

# Close the connection
conn.close()
print("MySQL connection closed.")
