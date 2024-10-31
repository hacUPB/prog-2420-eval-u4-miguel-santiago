def mostrar_menu(opciones):
    print("Seleccione una opcion")
    for i in opciones:
        print(f"{i}) {opciones[i][0]}")

def leer_opcion():

    Numero = input("Opcion :")

    while Numero not in opciones :
        print("Opcion no valida, regresando al inicio ")

    return Numero

def ejecutar_menu(opcion, opciones):
    opciones[opcion][1]()    #Buscar explicacion bien

def menu()
    opciones = {
        "1": ("Opc1":"eleg1")
        "2": ("Opc2":"eleg2")
        "3": ("Opc3":"eleg3")
        "4": ("Opc4":"eleg4")
        }

    generar_menu(opciones, "4")
