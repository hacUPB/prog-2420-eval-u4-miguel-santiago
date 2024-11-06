##LO QUE ME PIDEN:
#Debe proporcionar las siguientes opciones, donde cada opción llama a una **función** realizada para el caso específico:
#Contar número de palabras**: Debe contar el número de palabras en el archivo de texto y mostrar el resultado.
#Reemplazar una palabra por otra**: Debe permitir al usuario reemplazar una palabra por otra en el archivo de texto. La función debe recibir tanto la palabra a buscar, como la palabra por la que se tiene que reemplazar.

import os
def contar_palabras():  #Crear la función
    try: #try: El bloque try contiene el código que podría generar una excepción (un error). Python ejecuta este bloque de código, y si ocurre un error, salta al bloque except
        
        ruta_archivo = os.path.abspath(__file__)
        nombre = input("Ingrese el nombre del archivo (NO OLVIDE PONER .txt): ")

        ruta_de_documento = os.path.join(os.path.dirname(ruta_archivo), nombre)

        print("La ruta completa del archivo es:", ruta_de_documento)        
        with open(ruta_de_documento, 'r', encoding='UTF-8') as archivotxt:  #No es necesario cerrrar el archivo porque se utilza el with, este nos quita la preocupación de cerrar el archivo y no permite fugas o errores en los datos. Tambien se abre el archivo que se encuentra en la dirección que le proporcionamos a la variable. se abre en formato r+ que permite leer y escribir. 
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


import os
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



