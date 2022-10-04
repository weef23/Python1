### Ejemplo numero 1 interrupcion de un ciclo
def ejemplo1():
    for i in range(10000):
        print(f"Numero > {i}")
        ### Interrumpira el ciclo una vez llege a 5678
        if(i == 5678):
            break

### Ejemplo numero imprimir solamente numero pares entre el 1 y el 1000

def imprimirNumerosPares():
    for i in range(1000):
        ## La funcion continue lo que hacer es que contua obviando todo lo que este por debajo.
        if i % 2 != 0:
            continue
        print(f"Numero > {i}")
### Creamos un menu iteractivo para la ejecucion de las opciones
def run():
    menu = """
    Bienvenido por favor elija una opcion 💰💰
    1- Imprimir secuencia de numeros
    2- Imprimir numeros pares
    3- Salir 

    Seleccione una opcion por favor: 
    """
    ## Usamos un While para emular el menu de un sistema.
    while(True):
        opcion = input(menu)
        if opcion == '1':
            ejemplo1()
        elif opcion == '2':
            imprimirNumerosPares()
        elif opcion == '3':
            exit(0)
        else:
            print("Opcion incorrecta intentelo de nuevo")



if __name__ == "__main__":
    run()