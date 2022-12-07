from conection import cnxn


#----------------------------------------- Query a la base de Datos
def get_all_categories():
    cursor = cnxn.cursor()
    query = 'SELECT * FROM dbo.category'
    cursor.execute(query)
    categories = cursor.fetchall()
    cursor.close()
    #cnxn.close()
    return categories

def store(category):
    try:
        cursorInsert = cnxn.cursor()
        insert = "INSERT INTO category(id,name,description) VALUES (?,?,?)"
        cursorInsert.execute(insert, int(category['id']), category['name'], category['country'])
        cursorInsert.commit()
        cursorInsert.close()
        return category
    except:
        cursorInsert.execute("ROLLBACK")
        print("Ocurrio un error")
        
    

def search(id):
    query = "SELECT * FROM category WHERE id = "+id
    cursorSearch = cnxn.cursor()
    cursorSearch.execute(query)
    category = cursorSearch.fetchone()
    cursorSearch.close()
    return category

def update(id, category):
    name = category['name']
    country = category['country']
    cursorUpdate = cnxn.cursor()
    updated = "UPDATE category SET name = ?, description= ? WHERE id = ?"
    cursorUpdate.execute(updated , name, country, str(id))
    cursorUpdate.commit()
    cursorUpdate.close()
    return category
