######################## DICCIONARIOS EN PYTHON ###################################
### Los diccionarios son estructuras tipo clave valor #############################
def run():
    mi_diccionario = {
        'llave1': 1,
        'llave2': 2,
        'llave3': 3,
    }
    ##### Con el metodo key podemos acceder a las llaves
    for llave in mi_diccionario.keys():
        print(llave)
    ### Con el metodo value podemos acceder a los valores del diccionario
    for valores in mi_diccionario.values():
        print(valores)

    ### Tambien podemos extraer ambos con la funcion items
    for llave, items in mi_diccionario.items():
        print("La llave: '" + llave + "' contiene el item: " + str(items))


if __name__ == "__main__":
    run()