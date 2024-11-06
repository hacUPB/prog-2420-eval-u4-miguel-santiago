def listar_archivos_en_directorio():

    ruta_directorio = os.path.dirname(os.path.abspath(__file__))
    
    archivos = os.listdir(ruta_directorio)

    if archivos:
        print("ARCHIVOS EN EL DIRECTORIO ACTUAL:")
        for archivo in archivos:
            print(f"-{archivo}")
            print()
    else:
        print("No se encontraron archivos en el directorio.")
