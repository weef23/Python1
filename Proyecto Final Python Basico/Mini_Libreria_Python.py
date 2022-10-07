import json

########################################################################################################
####### Abre el archivo json en donde tenemos nuestra base de datos ####################################
def abrirBD():
    with open("../Datos/data.json") as data_base:
        data = json.load(data_base)
        return data
######### Visualizar seccion
def visualizarSeccion(datos):
    cont = 1
    print("Las secciones disponibles son las siguientes")
    for seccion in datos.keys():
        print(f"{cont} - {seccion}")
        cont+=1
    menu = """
            Que desea hacer? 
            1- Listar Libros disponibles
            2- Agregar un libro nuevo
            3- Salir
           
           Elija una opcion por favor: 
    """
    while True:
        opcion = input(menu)

        if opcion == '3':
            break
        elif opcion == '1':
            seccion = input("Escriba la seccion que desea visualizar ")
            visualizarLibros(datos,seccion)
        else:
            print("La opcion seleccionada no es correcta.")

#####  Visualizar libros
def visualizarLibros(data, seccion):

    seccion = data[seccion]

    for libro in seccion:
        print("Libro :")
        print(f" Autor: {libro['Autor']}")
        print(f" Titulo: {libro['Titulo']}")
        print(f" Editorial: {libro['Editorial']}")
        print(f" Area: {libro['Area']}")


############################################################################################################
def run():
    datos = abrirBD()
    ###### Visualizamos las secciones disponibles
    menu = """
           Bienvenido a mi mini biblioteca:
           
           1- Ver secciones disponibles
           2- Agregar Libro
           3- Agregar seccion
           4- Ingrese exit para salir del sistema 
           
           Seleccione una opcion: 
    """

    ##### Seleccionamos la seccion que deseamos visualizar

    while True:
        opcion = input(menu)

        if opcion == 'exit':
            exit(0)
        elif opcion == '1':
            visualizarSeccion(datos)
        else:
            print("Opcion incorrecta")

if __name__ == "__main__":
    run()
