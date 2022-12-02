from conection import cnxn

#----------------------------------------- Insert a la base de Datos
def transaction():
    try:
        cursorInsert = cnxn.cursor()
        insert = "INSERT INTO category(id,name,description) VALUES (?,?,?)"

        cursorInsert.execute(insert, 8, 'Pablo Balcaza', 'Peru')
        cursorInsert.execute(insert, 9, 'Miño Adrian', 'Peru')
        cursorInsert.execute(insert, 10, 'Cristian Galvez', 'Colombia')
        cursorInsert.execute(insert, 11, 'Walter Rollet', 'Canada')
        print('Successful Insert')
        cursorInsert.commit()
    except:
        cursorInsert.execute("ROLLBACK")
    else:
        cursorInsert.close()
        cnxn.close()
    
    

if __name__ == "__main__":
    transaction()