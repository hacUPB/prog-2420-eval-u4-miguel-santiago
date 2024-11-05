from FUNCION2 import contar_palabras

def mostrar_menu(opciones):
    print("Seleccione una opción")
    for i in opciones:
        print(f"{i}) {opciones[i][0]}") 

def leer_opcion(opciones):
    Numero = input("Digite su opción: ")
    while Numero not in opciones:
        print("Opción no válida, regresando al inicio") 
        Numero = input("Digite su opción: ")
    return Numero

def ejecutar_menu(opcion, opciones): 
    opciones[opcion][1]()  # Llama a la función correspondiente a la opción seleccionada

def generar_menu(opciones, opcion_salida):
    opcion = None
    while opcion != opcion_salida:
        mostrar_menu(opciones)
        opcion = leer_opcion(opciones)
        ejecutar_menu(opcion, opciones)
        print()

def menu():
    opciones = {
        "1": ("Listar archivos o conocer la ruta para buscarlos", eleg1),
        "2": ("Procesar archivos .txt", eleg2),
        "3": ("Procesar archivos .csv", eleg3),
        "4": ("Salir", salida)
    }
    generar_menu(opciones, "4")

def eleg1():
    print("Elegiste la opción 1")

def eleg2():
    print("Elegiste la opción 2: Contar palabras en un archivo.")
    contar_palabras()  # Llamada a contar_palabras

def eleg3():
    print("Elegiste la opción 3")

def salida():
    print("Saliendo")

if __name__ == "__main__":
    menu()
