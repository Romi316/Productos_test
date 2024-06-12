import csv
acum=0
lista=[]

def menu():
   print( 
    '''
    -.-.-.- M E N U -.-.-.-
    
    1.- Agregar producto
    2.- Listar todos los productos
    3.- Eliminar un producto por id
    4.- Generar archivo csv
    5.- Cargar datos desde csv
    6.- Estadísticas
    0.- Salir

    ''')
def agregar():
    id=input("Ingrese ID\n")
    nombre=input("Ingrese Nombre\n")
    precio=int(input("Ingrese Precio\n"))
    diccionario={'ID':id,'Nombre':nombre,'Precio':precio}
    lista.append(diccionario)
    print("Producto agregado exitosamente")
def printodos():
    for x in lista:
        print("ID: ", x['ID'], "Nombre: ",x['Nombre'], "Precio: ",x['Precio'])
        
def eliminar(a):
    encontrado=False
    for x in lista:
        if a== x['ID']:
            encontrado=True
            lista.remove(x)
            print("Producto eliminado correctamente")
            break
    if encontrado==False:
        print("El producto no existe...")   
             
            
while True:
    try:
        
        menu()
        op=int(input("Ingrese una opción \n"))
        
        if op==1:
            agregar()
        elif op==2:
            printodos()
        elif op==3:
            id=input("Ingrese ID para eliminar\n")
            eliminar(id)
        elif op==4:
            with open ('productos.csv','w',newline='') as productos:
                campos=['ID','Nombre','Precio']
                escritor=csv.DictWriter(productos,fieldnames=campos)
                escritor.writeheader()
                escritor.writerows(lista)
        elif op==5:
            lista.clear()
            with open('productos.csv','r',newline='') as productos:
                lector=csv.DictReader(productos)
                for x in lector:
                    lista.append(x)
            printodos()        
                
        elif op==6:
            for x in lista:
                acum = acum + int(x['Precio'])
            cantidad=len(lista)
            promedio=acum/cantidad
            print(f"El precio total de todos los productos es {acum}")
            print(f"El promedio del precio de los productos es {promedio}")  
        elif op==0:
            print("Adios!!")
        else:
            print("Comando desconocido, volviendo al menú...")    
    except:
        print("Error desconocido, volviendo al menú...")