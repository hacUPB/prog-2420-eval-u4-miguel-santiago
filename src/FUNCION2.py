##LO QUE ME PIDEN:
#Debe proporcionar las siguientes opciones, donde cada opción llama a una **función** realizada para el caso específico:
#Contar número de palabras**: Debe contar el número de palabras en el archivo de texto y mostrar el resultado.
#Reemplazar una palabra por otra**: Debe permitir al usuario reemplazar una palabra por otra en el archivo de texto. La función debe recibir tanto la palabra a buscar, como la palabra por la que se tiene que reemplazar.

def contar_palabras():  #CRear la función
    filename = input("Ingrese la dirección del texto (no olvidar poner .txt): ") #Ya que que no sabemos con que archivo se desea trabajar utilizamos la variable filename donde estará la dirección donde se encuentra el texto
    try: #try: El bloque try contiene el código que podría generar una excepción (un error). Python ejecuta este bloque de código, y si ocurre un error, salta al bloque except
        with open(filename, 'r') as f_obj:  #No es necesario cerrrar el archivo porque se utilza el with, este nos quita la preocupación de cerrar el archivo y no permite fugas o errores en los datos. Tambien se abre el archivo que se encuentra en la dirección que le proporcionamos a la variable. se abre en formato r+ que permite leer y escribir. 
            contenido = f_obj.read() #en la variable contenido se guarda todo el contenido que tiene el archivo de texto
    except FileNotFoundError: #except: Si ocurre una excepción dentro del bloque try, el flujo del programa se interrumpe y Python busca un bloque except que pueda manejar ese tipo de excepción. Si se encuentra, se ejecuta el código dentro de ese bloque.
        print(f"El archivo {filename} no existe.") #Esto se hace para que el usuario sea conciente de que se ha equivocado con la dirección del archivo
    else: #else: Se utiliza para que si no existe ninguna excepción el codigo fluya con normalidad
        palabras = contenido.split()  #se utiliza para dividir una cadena de texto (contenido) en una lista de palabras.
        numero_de_palabras = len(palabras) #cuenta el numero de palabras y las pone en una variable 
        print(f"Número de palabras en el archivo: {numero_de_palabras}") #imprime el numero de palabras
        return #Fin de la funcion


#Algunos comentarios utilizados arriba sirven de igual manera para el codigo de abajo por eso habrán lineas de codigo sin ellos.


def reemplazar_palabra():
    filename = input("Ingrese la dirección del texto (no olvidar poner .txt): ") 
    
    try:
        with open(filename, 'r+') as txtfile:
            contenido = txtfile.read()  #se guarda el contenido del texo dentro la variable contenido
    except FileNotFoundError:
        print(f"El archivo {filename} no existe.")
    else:
        palabras = contenido.split() #se utiliza para dividir una cadena de texto (contenido) en una lista de palabras.
        vieja_palabra = input("Ingrese la palabra a reemplazar: ") #Se pide la palabra que se va a cambiar
        nueva_palabra = input("Ingrese la nueva palabra: ") #Se pide la palabra por la que se va a camnbiar
        nuevo_contenido = contenido.replace(vieja_palabra, nueva_palabra) # se reemplazan las palabras
        print("Contenido modificado:")
        print(nuevo_contenido)
    return


##LO QUE ME PIDEN:
#Contar el número de caracteres: El programa debe calcular dos valores. El primero es el número total de caracteres, 
#incluidos los espacios en blanco, y el segundo es el número de caracteres sin contar los espacios en blanco. 
#Ambos resultados deben ser mostrados.
#data = var_archivo.read() 


def contar_numero_de_caracteres ():
     filename = input("Ingrese la dirección del texto (no olvidar poner .txt): ")
     fp = open( filename , 'r') #Se abre el archivo y se guarda en la variable fp
     datos = fp.read() #se leen todos los caracteres dentro del archivo y se guardan en datos
     fp.close()
     caracteres = len(datos) #cuenta el numero de datos
     print(f"el numero de caracteres contando los espacios es:{caracteres}") #imprime con el formato para llamar variables
     sin_espacios = datos.split( ) #entre los caracteres del archivo los separados con espacio se guardan en una lista
     caracteres_sin_espacios = sum(len(palabra) for palabra in sin_espacios) #se suma la cantidad de caracteres de cada palabra 
     print(f"el numero de caracteres sin contar los espacios es:{caracteres_sin_espacios}") 
     return


