

def new_func():
    def mostrar_menu(opciones):
        print("Seleccione una opcion")
        for i in opciones:
            print(f"{i}) {opciones[i][0]}") 

        



    def leer_opcion(opciones):
        Numero = input("Digite su opcion : ")
        while Numero not in opciones:
            print("Opcion no valida, regresando al inicio") 
            Numero = input("Digite su opcion : ")
        return Numero

    def ejecutar_menu(opcion, opciones): 
        opciones[opcion][1]()    #Opcion siendo la clave del diccionario donde buscaremos la informacio
                            #Opciones es el nombre del diccionario donde la clave tiene una cadena y el valor es una tupla donde el primer elemento es la opcion y el 
                            #segundo es la funcion que se ejecutara si el cliente selecciono esa opcion

    def generar_menu(opciones,opcion_salida):
        opcion = None
        while opcion != opcion_salida:
            mostrar_menu(opciones)
            opcion = leer_opcion(opciones)
            ejecutar_menu(opcion,opciones)
            print()



    def menu():
        opciones = {
        "1": ("Listar archivos o conocer la ruta para buscarlos",eleg1),
        "2": ("Procesar archivos .txt",eleg2),
        "3": ("Procesar archivos .csv",eleg3),
        "4": ("Salir",salida)
        }
        generar_menu(opciones, "4")
    





    def eleg1():
        print("Elegiste la opcion 1")

    def eleg2():
         print("Elegiste la opcion 2")

    def eleg3():
         print("Elegiste la opcion 3")

    def salida():
         print("Saliendo")






    if __name__=="__main__":
        menu()

return new_func()
