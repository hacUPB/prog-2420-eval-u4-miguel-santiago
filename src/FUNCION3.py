#LO PEDIDO:
#Mostrar las 15 primeras filas: con el fin de tener un vistazo rápido del documento que se va a analizar, esta función le permite al usuario observar el contenido de las primeras 15 líneas del archivo. Así, el usuario podrá decidir sus próximas acciones.
import os
import csv

def contenido_de_primeras_15_filas():
    try:

        ruta_archivo = os.path.abspath(__file__)
        nombre = input("Ingrese el nombre del archivo (NO OLVIDE PONER .csv): ")

        ruta_de_documento = os.path.join(os.path.dirname(ruta_archivo), nombre)

        print("La ruta completa del archivo es:", ruta_de_documento)

        with open(ruta_de_documento, 'r', newline='', encoding='utf-8') as csvfile:
            datos = csv.reader(csvfile)
            contador = 0
            for fila in datos:
                if contador < 15:
                    print(fila)
                    print( )
                    contador += 1
                else:
                    break

    except FileNotFoundError:
        print(f"El archivo en {ruta_de_documento} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        
contenido_de_primeras_15_filas()



def calular_estadistica():



def graficar():
    
