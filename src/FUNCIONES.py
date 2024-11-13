import os  


def listar_archivos_en_directorio():
    ruta_directorio = os.path.dirname(os.path.abspath(__file__))  # os.path.abspath(__file__) devuelve la ruta absoluta del archivo actual
    archivos = os.listdir(ruta_directorio)  # os.listdir() devuelve una lista con los nombres de los archivos en el directorio
    print("Archivos en el directorio actual:")
    for archivo in archivos:
        print(archivo)
        print()  # Salto de línea para mejorar la legibilidad de la salida.
    else:  # Si no hay archivos en el directorio
        print("No se encontraron archivos en el directorio.")




### FUNCION 2

##LO QUE ME PIDEN:
#Debe proporcionar las siguientes opciones, donde cada opción llama a una **función** realizada para el caso específico:
#Contar número de palabras**: Debe contar el número de palabras en el archivo de texto y mostrar el resultado.
#Reemplazar una palabra por otra**: Debe permitir al usuario reemplazar una palabra por otra en el archivo de texto. La función debe recibir tanto la palabra a buscar, como la palabra por la que se tiene que reemplazar.


def contar_palabras():  #Crear la función
    try: #try: El bloque try contiene el código que podría generar una excepción (un error). Python ejecuta este bloque de código, y si ocurre un error, salta al bloque except
        
        ruta_archivo = os.path.abspath(__file__)
        nombre = input("Ingrese el nombre del archivo (NO OLVIDE PONER .txt): ")

        ruta_de_documento = os.path.join(os.path.dirname(ruta_archivo), nombre)

        print("La ruta completa del archivo es:", ruta_de_documento)        
        with open(ruta_de_documento, 'r', encoding='latin1') as archivotxt:  #No es necesario cerrrar el archivo porque se utilza el with, este nos quita la preocupación de cerrar el archivo y no permite fugas o errores en los datos. Tambien se abre el archivo que se encuentra en la dirección que le proporcionamos a la variable. se abre en formato r+ que permite leer y escribir. 
            contenido = archivotxt.read() 
            palabras = contenido.split()  #se utiliza para dividir una cadena de texto (contenido) en una lista de palabras.
            numero_de_palabras = len(palabras) #cuenta el numero de palabras y las pone en una variable 
            print(f"Número de palabras en el archivo: {numero_de_palabras}") #imprime el numero de palabras#en la variable contenido se guarda todo el contenido que tiene el archivo de texto
    except FileNotFoundError: #except: Si ocurre una excepción dentro del bloque try, el flujo del programa se interrumpe y Python busca un bloque except que pueda manejar ese tipo de excepción. Si se encuentra, se ejecuta el código dentro de ese bloque.
        print(f"El archivo {nombre} no existe.") #Esto se hace para que el usuario sea conciente de que se ha equivocado con la dirección del archivo
         #else: Se utiliza para que si no existe ninguna excepción el codigo fluya con normalidad
    except Exception as e:
        # Captura cualquier otro tipo de excepción que pueda ocurrir
        print(f"Ocurrió un error: {e}")
        return #Fin de la funcion


def reemplazar_palabra():

    
    try:
        ruta_archivo = os.path.abspath(__file__)
        nombre = input("Ingrese el nombre del archivo (NO OLVIDE PONER .txt): ")

        ruta_de_documento = os.path.join(os.path.dirname(ruta_archivo), nombre)
    
        with open(ruta_de_documento, 'r+', encoding='latin1') as txtfile:
            contenido = txtfile.read()  #se guarda el contenido del texo dentro la variable contenido

            vieja_palabra = input("Ingrese la palabra a reemplazar: ") #Se pide la palabra que se va a cambiar
            nueva_palabra = input("Ingrese la nueva palabra: ") #Se pide la palabra por la que se va a camnbiar
            nuevo_contenido = contenido.replace(vieja_palabra, nueva_palabra) # se reemplazan las palabras
            print("Contenido modificado:")
            print(nuevo_contenido)
    except FileNotFoundError:
        print(f"El archivo {nombre} no existe.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return


##LO QUE ME PIDEN:
#Contar el número de caracteres: El programa debe calcular dos valores. El primero es el número total de caracteres, 
#incluidos los espacios en blanco, y el segundo es el número de caracteres sin contar los espacios en blanco. 
#Ambos resultados deben ser mostrados.
#data = var_archivo.read() 



def contar_numero_de_caracteres():
    try:

        ruta_archivo = os.path.abspath(__file__) 
        nombre = input("Ingrese el nombre del archivo (NO OLVIDE PONER .txt): ")

        ruta_de_documento = os.path.join(os.path.dirname(ruta_archivo), nombre)

        with open(ruta_de_documento, 'r', encoding= 'latin1') as txtfile:
            datos = txtfile.read()
        

            caracteres = len(datos)
            print(f"El número de caracteres contando los espacios es: {caracteres}")
        

            sin_espacios = datos.split()  
            caracteres_sin_espacios = sum(len(palabra) for palabra in sin_espacios)
            print(f"El número de caracteres sin contar los espacios es: {caracteres_sin_espacios}")
    
    except FileNotFoundError:
        print("El archivo no se encuentra. Verifique la dirección ingresada.")
    except Exception as e:
        print(f"Ocurrió un error: {e}")
        return

###FUNCION 3

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
        


def estadistica():
    try:
        ruta_archivo = os.path.abspath(__file__)
        Archivo = input("Ingrese el nombre del archivo CSV: ").strip()
        ruta_de_documento = os.path.join(os.path.dirname(ruta_archivo), Archivo)

        with open(ruta_de_documento, 'r', encoding='utf-8') as CSv:
            c = input("Ingrese con qué caracter requiere delimitar las columnas: ")
            leer = csv.reader(CSv, delimiter=c)
            Columnas = next(leer)
            print("Las columnas disponibles son", Columnas)
            columna = input("¿Qué columna desea analizar? Escribe el nombre de la columna: ").strip()

        if columna in Columnas:
            Numero = Columnas.index(columna)
            datos = []

            for fila in leer:
                try:
                    valor = float(fila[Numero])
                    datos.append(valor)
                except ValueError:
                    continue

            if datos:
                datos.sort()
                cantidad = len(datos)
                Maximo = max(datos)
                Minimo = min(datos)
                Prome = sum(datos) / cantidad
                Mitad = cantidad // 2

                if cantidad % 2 == 1:
                    Mediana = datos[Mitad]
                else:
                    Mediana = (datos[Mitad - 1] + datos[Mitad]) / 2

                print(f"El valor máximo es {Maximo}, y el valor mínimo es {Minimo}.")
                print(f"El promedio es {Prome}, y la mediana es {Mediana}.")
    except FileNotFoundError:
        print("El archivo CSV no se encontró en la ruta especificada.")
                




def graficar():
    try:
        ruta_archivo = os.path.abspath(__file__)
        Archivo = input("Ingrese el nombre del archivo CSV: ").strip()
        ruta_de_documento = os.path.join(os.path.dirname(ruta_archivo), Archivo)

        with open(ruta_de_documento, 'r', encoding='utf-8') as CSv:
            b = input("Ingrese con qué carácter requiere delimitar las columnas: ")
            leer = csv.reader(CSv, delimiter=b)
            Columnas = next(leer)
            print("Las columnas disponibles son", Columnas)
            columna = input("¿Qué columna desea graficar? Escribe el nombre de la columna: ").strip()

        if columna in Columnas:
            Numero = Columnas.index(columna)
            datos = []

            for fila in leer:
                try:
                    valor = float(fila[Numero])
                    datos.append(valor)
                except ValueError:
                    continue

            if datos:
                gra.plot(datos)
                gra.title(f"Gráfico de la columna: {columna}")
                gra.show()
            else:
                print("No hay datos numéricos en la columna seleccionada.")
        else:
            print("La columna no existe en el archivo.")
    except FileNotFoundError:
        print("El archivo CSV no se encontró en la ruta especificada.")


    




    
