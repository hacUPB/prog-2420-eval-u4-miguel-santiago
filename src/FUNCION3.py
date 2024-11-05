#LO PEDIDO:
#Mostrar las 15 primeras filas: con el fin de tener un vistazo rápido del documento que se va a analizar, esta función le permite al usuario observar el contenido de las primeras 15 líneas del archivo. Así, el usuario podrá decidir sus próximas acciones.
import csv
def contenido_de_primeras_15_filas():
    ubicacion_archivo = input("ingrese la direccion del archivo con la terminación (.csv)")
    try: 
        with open(ubicacion_archivo, 'r' ,newline='') as csvfile: 
            datos = csv.reader(csvfile)
    except FileNotFoundError:
        print(f"El archivo en {ubicacion_archivo} no existe.")  
    else:            
        contador = 0
        for fila in datos:
            if contador < 15:
                print(fila)
                contador += 1
            else:
                    break
            return
contenido_de_primeras_15_filas()



import csv

def contenido_de_primeras_15_filas():
    # Solicitar la ubicación del archivo
    ubicacion_archivo = input("Ingrese la dirección del archivo con la terminación (.csv): ")
    
    try:
        # Intentamos abrir el archivo
        with open(ubicacion_archivo, 'r', newline='', encoding='utf-8') as csvfile:
            # Intentamos leer el archivo con el delimitador común (coma por defecto)
            datos = csv.reader(csvfile)
    except FileNotFoundError:
        print(f"El archivo en {ubicacion_archivo} no existe.")
    except Exception as e:
        print(f"Ocurrió un error al abrir el archivo: {e}")
    else:
        contador = 0
        # Iteramos sobre las filas del CSV
        for fila in datos:
            if contador < 15:
                print(fila)  # Imprime cada fila
                contador += 1
            else:
                break  # Sale después de imprimir las 15 filas
        return

contenido_de_primeras_15_filas()
