### Importamos el modulo que nos permite trabajar con archivos JSON
import json

### Abrimos el Archivo JSON que deseamos abrir
with open("./Datos/data.json") as bd_libros:
    data = json.load(bd_libros)

    ## Veamos que tipo de datos nos trajo al abrir el JSON
    print(f"Type: {type(data)}") ## Nos trae un tipo de dato Diccionario

    ### Nos traemos la seccion algebra de nuestra base de datos
    seccion = data["Algebra"]
    ### Imprimimos los libros de cada una de las secciones de la libreria
    for libro in seccion:
        print("Libro :")
        print(f" Autor: {libro['Autor']}")
        print(f" Titulo: {libro['Titulo']}")
        print(f" Editorial: {libro['Editorial']}")
        print(f" Area: {libro['Area']}")
