def cargar_archivo(ruta):

    with open(ruta) as archivo:
        for linea in archivo:
            yield linea.strip("\n")