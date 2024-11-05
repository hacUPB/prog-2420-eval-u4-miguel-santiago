#Debe proporcionar las siguientes opciones, donde cada opción llama a una **función** realizada para el caso específico:
#Contar número de palabras**: Debe contar el número de palabras en el archivo de texto y mostrar el resultado.
#Reemplazar una palabra por otra**: Debe permitir al usuario reemplazar una palabra por otra en el archivo de texto. La función debe recibir tanto la palabra a buscar, como la palabra por la que se tiene que reemplazar.

def contar_palabras():  #CRear la función
    filename = input("Ingrese la dirección del texto (no olvidar poner .txt): ") #Ya que que no sabemos con que archivo se desea trabajar utilizamos la variable filename donde estará la dirección donde se encuentra el texto
    try: #try: El bloque try contiene el código que podría generar una excepción (un error). Python ejecuta este bloque de código, y si ocurre un error, salta al bloque except
        with open(filename, 'r+') as f_obj:  #No es necesario cerrrar el archivo porque utilza el with
            contenido = f_obj.read()
    except FileNotFoundError: #except: Si ocurre una excepción dentro del bloque try, el flujo del programa se interrumpe y Python busca un bloque except que pueda manejar ese tipo de excepción. Si se encuentra, se ejecuta el código dentro de ese bloque.
        print(f"El archivo {filename} no existe.")
    else: 
        palabras = contenido.split()
        numero_de_palabras = len(palabras)
        print(f"Número de palabras en el archivo: {numero_de_palabras}")
        return





def reemplazar_palabra():
    filename = input("Ingrese la dirección del texto (no olvidar poner .txt): ")
    
    try:
        with open(filename, 'r+') as txtfile:
            contenido = txtfile.read()
    except FileNotFoundError:
        print(f"El archivo {filename} no existe.")
        
    palabras = contenido.split()
    vieja_palabra = input("Ingrese la palabra a reemplazar: ")
    nueva_palabra = input("Ingrese la nueva palabra: ")
    nuevo_contenido = contenido.replace(vieja_palabra, nueva_palabra)
    print("Contenido modificado:")
    print(nuevo_contenido)
    return



#Contar el número de caracteres: El programa debe calcular dos valores. El primero es el número total de caracteres, 
#incluidos los espacios en blanco, y el segundo es el número de caracteres sin contar los espacios en blanco. 
#Ambos resultados deben ser mostrados.
#data = var_archivo.read() 


def contar_numero_de_caracteres ():
     filename = input("Ingrese la dirección del texto (no olvidar poner .txt): ")
     fp = open( filename , 'r')
     datos = fp.read()
     fp.close()
     caracteres = len(datos)
     print(f"el numero de caracteres contando los espacios es:{caracteres}")
     sin_espacios = datos.split( )
     caracteres_sin_espacios = sum(len(palabra) for palabra in sin_espacios)
     print(f"el numero de caracteres sin contar los espacios es:{caracteres_sin_espacios}")
     return


