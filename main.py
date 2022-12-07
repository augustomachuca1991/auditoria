import categories as ct
import csv
import sys, signal, time
from os import system

def listCategories():
    categories = ct.get_all_categories()
    for category in categories:
        print(category)

def createFile():
    timestr = time.strftime("%Y%m%d-%H%M%S")
    fileName = 'categories'+timestr+'.csv'
    categories = ct.get_all_categories()
    with open(fileName, 'w', newline='') as csvfile:
        fieldnames = ['id','name','country']
        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()
        for category in categories:
            writer.writerow({'id': category[0], 'name': category[1] , 'country' :category[2] })
    print('archivo creado')

def createCategory():
    id = input('Ingrese Cod: ')
    name = input('Ingrese Nombre: ')
    country = input('Ingrese Pais: ')
    category = {'id' : id , 'name' : name, 'country' : country}
    ct.store(category=category)
    print(f'nueva categoria{category}')

def editCategory():
    id = input('\nIngrese el id del registro que desea editar: ')
    isCategory = ct.search(id)
    if isCategory:
        category = {'name' : 'nombre editado', 'country' : 'pais editado'}
        editCategory = ct.update(id=isCategory[0], category=category)
        print(editCategory)


def findCategory():
    id = input('\nIngrese el id que desea buscar: ')
    category = ct.search(id)
    if category:
        print(category)
    




def sig_handler(sig, frame):
    print('\n[*] Exiting... \n')
    sys.exit(0)

signal.signal(signal.SIGINT, sig_handler)

if __name__ == "__main__":
    while True:
        print('##################-MENU-#############################')
        print('1 - Listar Categorias')
        print('2 - Crear Categoria')
        print('3 - Editar Categoria')
        print('4 - Detalle Categoria')
        print('5 - Crear CSV de Categorias')
        print('Ctrl + c para Salir')
        print('####################################################')
        option = input('Ingrese una opcion: ')
        if option == '1':
            listCategories()
        elif option == '2':
            createCategory()
        elif option == '3':
            editCategory()
        elif option == '4':
            findCategory()
        elif option == '5':
            createFile()
        else:
            print('Opcion invalida')
        time.sleep(2)