##import pytds
from decouple import config
import pyodbc

driver = 'SQL server'
server = config('MSSQL_SERVER')
db = config('MSSQL_DB')
username = config('MSSQL_USER')
password = config('MSSQL_PASSWORD')
port= config('MSSQL_PORT')

try:
    cnxn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};SERVER='+server+';DATABASE='+db+';UID='+username+';PWD='+ password)
    # with pytds.connect(server, db, username, password) as conn:
    #     with conn.cursor() as cur:
    #         cur.execute("select * from category")
    #         query = cur.fetchall()
    #         print(query)        
except Exception as ex:
    print(ex)