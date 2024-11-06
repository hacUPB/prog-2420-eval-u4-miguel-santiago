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


    import csv

import os

def graficar():





   

    try:

        ruta_archivo = os.path.abspath(__file__)
        Archivo = input("Ingrese el nombre del archivo CSV: ").strip()
        ruta_de_documento = os.path.join(os.path.dirname(ruta_archivo), Archivo)

        with open(ruta_de_documento,'r', encoding='utf-8') as CSv:
            b = input("Ingrese con que caracter requiere delimitar las columnas")
            leer = csv.reader(CSv,delimiter=b )
            Columnas = next(leer)
            print("Las columnas disponibles son")
            for C,Columnas in enumerate(Columnas, start= 1 ): 
                print (f"{C}. {Columnas}")
                print()

            columna = input("Que columna desea graficar? Escribe el nombre de la columna: ").upper().strip()
            if columna in Columnas:
                Numero_columna = Columnas.index(columna)#Me dice la posicion de la columna
                print(Numero_columna)

            if columna in [columna.upper() for columna in Columnas]:  # Verificar si la columna existe
                Numero_columna = Columnas.index(columna)  # Obtener el índice de la columna
                print(f"La columna seleccionada es: {columna} (Índice {Numero_columna})")
                
                # Leer todas las filas y obtener los datos de la columna seleccionada
                datos_columna = []
                for fila in leer:
                    try:
                        # Convertir los datos a número (float) si es posible
                        datos_columna.append(float(fila[Numero_columna]))
                    except ValueError:
                        # Si no es un número válido, puedes ignorar o manejar el error de alguna manera
                        continue

                if datos_columna:
                    # Graficar los datos
                    plt.plot(datos_columna)
                    plt.title(f"Gráfico de la columna: {columna}")
                    plt.xlabel('Índice de fila')
                    plt.ylabel(f'Valores de {columna}')
                    plt.show()
                else:
                    print(f"No se pudieron obtener datos numéricos de la columna '{columna}'.")
            else:
                print(f"La columna '{columna}' no existe en el archivo.")

    except FileNotFoundError:
        print("El archivo no fue encontrado. Asegúrate de que el nombre sea correcto.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")

# Llamada a la función para graficar
graficar()



















    except FileNotFoundError:
        print("El archivo no fue encontrado. Asegúrate de que el nombre sea correcto.")
    
graficar()




def graficar():
    
