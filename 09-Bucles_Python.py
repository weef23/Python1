############ Ejemplo de Bucles en Python ########################

### Ejemplo de un bucle while
def ejemploBucleWhile():
    limite = 10
    contador = 0
    potencia = 2**contador

    while contador < limite:
        print(f"2 elevado a {contador} es igual a {potencia}")
        contador= contador + 1
        potencia= 2**contador

### Ejemplo con el bucle for
def ejemploCicloFor():

    for i in range(0,100):
        potencia = 2 ** i
        print(f"2 elevado a {i} es igual a {potencia}")

def ejemploBusquedaFor():
    listaValores = [1,4,8,12,16,20,24,28,32]
    ## Digite el numero que desea buscar
    busqueda = int(input("Digite el numero que desea buscar => "))

    contador = 0
    for numero in listaValores:
        if numero == busqueda:
            print("Numero encontrado con exito")
            contador += 1
        else:
            continue
    else:
        print(f"Se encontraron {contador} resultados") if contador > 0 else print("No se encontro ningun resultado")


def run():
    print("Ejecucion de ciclo While \n")
    ejemploBucleWhile()

    print("Ejecucion de ciclo For \n")
    ejemploCicloFor()

    print("Ejemplo de busqueda usando ciclos for:\n")
    ejemploBusquedaFor()


if __name__ == "__main__":
    run()