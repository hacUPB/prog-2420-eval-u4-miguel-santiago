from FUNCION2 import contar_palabras

def mostrar_menu(opciones):
    print("Seleccione una opción")#Genero una funcion donde genero las opciones del menu y las muestro con la variable i para que asi recorra cada una de las claves en el diccionario llamado "opciones" 
    for i in opciones:
        print(f"{i}) {opciones[i][0]}")#Imprimo cada i el cual es la clave de cada diccionario y asi despues poder llamar la tupla y separarlo desde la columna 0 y asi llamar la funcion mas adelante

def leer_opcion(opciones):
    Numero = input("Digite su opción: ") #Con una variable indico la opcion que se debe digitar
    while Numero not in opciones:
        print("Opción no válida, regresando al inicio")  #Creo un bucle con el while para que el numero que si digite o la opcion, sea correcta y se encuentre dentro del diccionario opciones
        Numero = input("Digite su opción: ").strip() #Digito nuevamente el numero para asegurar de cumpli con el bucle hasta poner la opcion correcta y adiciono el strip por un error cuando corria el codgio y funciono entonces lo dejo 
    return Numero                              #strip es para eliminar los espacios en blanco cuando se digite

def ejecutar_menu(opcion, opciones): 
    opciones[opcion][1]()  # ejecuto el menu con la funciones adentro que voy a llamar, las cuales son opcion y opciones para asi llamar opciones el diccionario, e imprimo todo el menu por medio de las tuplas del diccionario donde la primera
    #opcion es (0) la descripciom del menu, y la segunda posicion es (1) para llamar la funcion cuando seleccione esta opcion 

def generar_menu(opciones, opcion_salida): #Asi genero el menu donde empiezo a llamar todas las funciones anteriores, y creo la variable opcion, para que inicie un bucle diferente a vacio(None) y mostrar todoas las funciones
    
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones) #Genero la misma variable opcion para que Numero sea leido
        ejecutar_menu(opcion, opciones)#indico que debo de ejecturar para reañizar el menu por medio de la funcion
        print()#Asi puedo imprimir todo lo anterior que llame en cada funcion

def menu():#Diccionario de las opciones a elegir junto con las tuplas que llaman a cierta funcion cuando se digita el numero de la opccion
    opciones = {
        "1": ("Listar archivos o conocer la ruta para buscarlos", eleg1),
        "2": ("Procesar archivos .txt", eleg2),
        "3": ("Procesar archivos .csv", eleg3),
        "4": ("Salir", salida)
    }
    generar_menu(opciones, "4") #Aqui es como genero la salida indicando el numero de opciones e imprimiendo cada diccionario junto con la funcion salida del menu

def sub_menu2():
    opciones2 = {
        "A": ("Contar palabras del arcivho .txt", Eleccion1),
        "B": ("Remplazar palabras del arcivho .txt", Eleccion2),
        "C": ("Contar numero de caracteres del arcivho .txt", Eleccion3),
        "D": ("Volver al menu principal", Salida)
        
    }
    
    generar_menu("sub_menu2", opciones2, "C")




def eleg1():
    print("Elegiste Listar archivos o buscarlos")

def eleg2():
    print("Elegiste Procesar archivos .csv")

    
    
def eleg3():
    print("Elegiste Procesar archivos .csv")

def salida():
    print("Saliendo")
   
   
#Realizo las otras funciones para llamar al submenu dentro del menu 

def Eleccion1():
    print("Elegiste contar numero de palabras")

def Eleccion2():
    print("Elegiste remplazar una palabra")
    contar_palabras()
    
    
    
def Eleccion3():
    print("Elegiste contar numero de caracteres")

def Salida():
    print("Saliendo al menu principal")
    
    

if __name__ == "__main__":
    menu()
