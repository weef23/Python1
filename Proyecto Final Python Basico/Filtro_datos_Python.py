##################################### DICCIONARIO ####################################################################
import Diccionario_Busqueda as db ## Importamos el diccionario que tenemos en el otro documento.

######################################################################################################################
def run():
    ## Filtramos todos los individuos que son expertos en python
    workers_python = [worker["name"] for worker in db.DATA if worker['language'] == 'python' ]
    workers_platzi = [worker["name"] for worker in db.DATA if worker['organization'] == 'Platzi']

    ### USO DE FILTER Y DE MAP PARA HACER UNA BUSQUEDA DENTRO DE UNA LISTA
    adultos = list(filter(lambda worker: worker['age'] >= 18, db.DATA))
    adultos = list(map(lambda worker: worker['name'], adultos))

    ## Agrega una nueva clave valor al diccionario utilizando map y el pip para concatenar diccionarios
    ## Solo funciona para python 3.9 en adelante
    ##adulto_mayor = list(map(lambda worker: worker | {"old":worker['age'] > 70}, db.DATA ))
    print("Expertos en Python")
    for w in workers_python:
        print(w)

    print("Expertos de Platzi")
    for w in workers_platzi:
        print(w)

    print("Adultos ")
    for w in adultos:
        print(w)
########################################################################################################################
## Funcion de arranque de librerias.
if __name__ == "__main__":
    run()

