def listar_archivos_en_directorio():

    ruta_directorio = os.path.dirname(os.path.abspath(__file__))  # os.path.abspath(__file__) devuelve la ruta absoluta del archivo actual, 
                                                                  # y os.path.dirname() extrae el directorio sin incluir el nombre del archivo.
    
    archivos = os.listdir(ruta_directorio)  # Devuelve una lista con los nombres de los archivos presentes en el directorio actual (como cadenas de texto).

    if archivos:  # Condicional para verificar si hay archivos en el directorio
        print("ARCHIVOS EN EL DIRECTORIO ACTUAL:")
        for archivo in archivos:  # Itera sobre la lista de archivos y muestra cada uno en formato de lista
            print(f"- {archivo}")
            print()  # Salto de línea para mejorar la legibilidad de la salida.
    else:  # Si no hay archivos en el directorio
        print("No se encontraron archivos en el directorio.")
