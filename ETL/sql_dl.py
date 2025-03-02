import mysql.connector
import pandas as pd

# Replace these with your database details
username = 'root'              # Your MySQL username (default for XAMPP is 'root')
password = ''                  # Your MySQL password (default for XAMPP is '' (empty))
database_name = 'sample_nlp_5'       # Your database name
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

query = "SELECT * FROM users;"

df4 = pd.read_sql(query,conn)
print(df4)