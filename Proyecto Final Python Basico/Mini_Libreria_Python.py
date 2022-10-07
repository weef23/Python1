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
