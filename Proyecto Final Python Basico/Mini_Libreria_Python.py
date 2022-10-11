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
        cont += 1
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
            visualizarLibros(datos, seccion)
        elif opcion == '2':
            seccion = input("Escriba la seccion donde desea agregar el libro: ")
            agregarLibro(datos,seccion)
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

#### Agrega una nuevo libro a la seccion que nosotros elijamos.
def agregarLibro(data, seccion):
    nuevoLibro = {}

    ##### Solicitamos el autor del libro
    autor = input("Ingrese por el autor del libro: ")
    #### Solicitamos el Titulo del Libro
    titulo = input("Ingrese el titulo del libro: ")
    ### Solicitamos la editorial del libro
    editorial = input("Ingrese la editorial del libro: ")
    ### Solicitamos el Area del Libro
    area = input("Solicitamos el area del libro: ")

    #### Agregamos el nuevo libro a la biblioteca
    nuevoLibro.update({"Autor": autor})
    nuevoLibro.update({"Titulo": titulo})
    nuevoLibro.update({"Editorial": editorial})
    nuevoLibro.update({"Area": area})

    seccionLibros = data[seccion]
    ## Las listas en python al asignarse a otra varible los que hacemos realmente
    ## es reasignar la referencia hacia otra variable, por lo que cualquier cambio
    ## que hagamos en la lista la anterior la conservara, nos aprovecharemos de este
    ## comportamiento para agregar un nuevo registro a nuestra mini biblioteca.
    seccionLibros.append(nuevoLibro)
    ### Visualizaos la seccion que acabamos de modificar
    visualizarLibros(data, seccion)


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
