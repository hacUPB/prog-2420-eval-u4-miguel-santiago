#Debe proporcionar las siguientes opciones, donde cada opción llama a una **función** realizada para el caso específico:
#Contar número de palabras**: Debe contar el número de palabras en el archivo de texto y mostrar el resultado.
#Reemplazar una palabra por otra**: Debe permitir al usuario reemplazar una palabra por otra en el archivo de texto. La función debe recibir tanto la palabra a buscar, como la palabra por la que se tiene que reemplazar.

def contar_palabras():
    filename = input("Ingrese la dirección del texto (no olvidar poner .txt): ")
    try:
        with open(filename, 'r') as f_obj:
            contenido = f_obj.read()
    except FileNotFoundError:
        print(f"El archivo {filename} no existe.")
    else:
        palabras = contenido.split()
        numero_de_palabras = len(palabras)
        print(f"Número de palabras en el archivo: {numero_de_palabras}")

contar_palabras()
