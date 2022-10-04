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

def run():
    print("Ejecucion de ciclo While \n")
    ejemploBucleWhile()

    print("Ejecucion de ciclo For \n")
    ejemploCicloFor()


if __name__ == "__main__":
    run()