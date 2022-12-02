from conection import cnxn


#----------------------------------------- Query a la base de Datos
def transactionDB():
    try:
        cursor = cnxn.cursor()
        query = 'SELECT * FROM dbo.category'
        cursor.execute(query)
        categories = cursor.fetchall()
        for category in categories:
            print(category)
    except:
        cursor.execute("ROLLBACK")
    else:
        cursor.close()
        cnxn.close()

    
    

if __name__ == "__main__":
    transactionDB()