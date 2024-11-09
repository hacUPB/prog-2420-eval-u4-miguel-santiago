#LO PEDIDO:
#Mostrar las 15 primeras filas: con el fin de tener un vistazo rápido del documento que se va a analizar, esta función le permite al usuario observar el contenido de las primeras 15 líneas del archivo. Así, el usuario podrá decidir sus próximas acciones.
import csv
import matplotlib.pyplot as gra
import os

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
        




import csv
import matplotlib.pyplot as gra
import os

import csv


def estadistica()


    try:

        ruta_archivo = os.path.abspath(__file__)
        Archivo = input("Ingrese el nombre del archivo CSV: ").strip()
        ruta_de_documento = os.path.join(os.path.dirname(ruta_archivo), Archivo)

        with open(ruta_de_documento,'r', encoding='utf-8') as CSv:
            c = input("Ingrese con que caracter requiere delimitar las columnas")
            leer = csv.reader(CSv,delimiter=c )
            Columnas = next(leer) #Realiza el salto entre columnas
            print("Las columnas disponibles son")
            columna = input("Que columna desea realizar la estadistica? Escribe el nombre de la columna: ").upper().strip()


        if columna in Columnas:
            Numero = Columnas.index(columna)#Me dice la posicion de la columna
            datos = []

            #Hasta aqui es el mismo codigo que la funcion de graficar
            #Se identifican las columnas y se selecciona una

        for fila in leer:
            try:
                valor = float(fila[Numero])  # Si el valor no es un numero, aqui se convierte con float para poderlo graficar
                datos.append(valor)  # Se agrega el valor a datos que esta vacio
            except ValueError:
                 
                continue
            
            #Hasta aqui es el mismo codigo que la funcion de graficar
            #Se identifican las columnas y se selecciona una

            #Aqui inicia el nuevo codigo base para las estadisticas

            if datos:
                datos.sort()   #Aqui esta guardada toda la informacion de la columna
                cantidad = len(datos)
                Maximo = max(datos)
                Minimo = min(datos)
                Prome = sum(datos)/cantidad
                Mitad = cantidad // 2 # Realiza una division entera, eliminando asi decimales
                
                if cantidad % 2 == 1:  #Se identifica si es par o impar
                    mediana = datos[Mitad] #Si es impar, se logra con facilidad la mediana
                else:
                    Mediana = (datos[Mitad-1] + datos [Mitad]) / 2   # Esto se hace en caso de que sea par
                    #Es el promedio de la suma de los dos valores del medio

                print (f"El valor maximo es {Maximo}, y el valor minimo es {Minimo} ")
                print (f"El promedio es {Prome}, y la mediana es {Mediana} ")


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
            columna = input("Que columna desea graficar? Escribe el nombre de la columna: ").upper().strip()


        if columna in Columnas:
            Numero = Columnas.index(columna)#Me dice la posicion de la columna
            datos = []

            

            for fila in leer:
                try:
                    valor = float(fila[Numero])  # Si el valor no es un numero, aqui se convierte con float para poderlo graficar
                    datos.append(valor)  # Se agrega el valor a datos que esta vacio
                except ValueError:
                 
                    continue
            
            # Se Grafican los datos, se deben probar muy bien para que los resultados deseados sean los correctos
            if datos:
                gra.plot(datos)
                gra.title(f"Gráfico de la columna: {columna}")
                gra.show()
            else:
                print("No hay datos numéricos en la columna seleccionada.")
        else:
            print("La columna no existe en el archivo.")



    
