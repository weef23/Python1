#### Valida que el valor introducido sea un numero
def verificarValor(valor):
    if str.isnumeric(valor):
        return int(valor)
    else:
        print("Solo es posible convertir valores numericos")
        exit(0)

####################################################################################################
#################### Funcion que valida si un numero es primo #####################################
def esNumeroPrimo(numero):
    contador = 0
    ### Para saber si un numero es primo solo basta con dividirlo entre los primero primos.
    primos = [2,3,5,7,11]

    for i in primos:
        if numero % i == 0 and numero!=i:
            contador += 1

    if contador == 0:
        print(f"Es numero {numero} es un numero primo")
    else:
        print(f"Es numero {numero} no es un numero primo")

###########################################################################################################
def run():
    menu = """
          Bienvenido por favor elija una opcion 💰💰
          1- Validar si un numero es Primo
          2- Salir 

          Seleccione una opcion por favor: 
          """
    while True:
        opcion = input(menu)

        if opcion == '1':
            numero = verificarValor(input("Digite un numero: "))
            esNumeroPrimo(numero)
        elif opcion == '2':
            exit(0)
        else:
            print("Opcion incorrecta")

#####################################################################################
if __name__ == "__main__":
    run()
