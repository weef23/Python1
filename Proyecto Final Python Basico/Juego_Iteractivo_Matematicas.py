import random

def verificarValor(valor):
    if (str.isnumeric(valor)):
        return int(valor)
    else:
        print("Solo es posible convertir valores numericos")
        exit(0)

############################Funcion Aprende a sumar#####################################################################
def aprenderSumar():
    contador = 0
    for i in range(1, 10):
        a = random.randint(1, 100)
        b = random.randint(1, 100)
        resultado = verificarValor(input(f"Digite el resultado de la suma de {a} + {b} : "))
        if (a + b) == resultado:
            contador += 1
    return (contador / 10) * 100


##################### Tablas de Multiplicar #################################################################
def aprenderTablasMultiplicar(tabla):
    contador = 0
    for i in range(1, 10):
        resultado = verificarValor(input(f"Digite el resultado de multiplicar {i} * {tabla} : "))

        if resultado == (i * tabla):
            contador += 1
    return (contador / 10) * 100


#################################################################################################################
def run():
    menu = """
    Bienvenido a MateFacil elija un reto por favor:
    1- Reto de la suma de numeros aleatoreos.
    2- Reto de las tablas de multiplicar.
    3- Reto de los numeros primos
    4- Salir.
    Por favor elija una opcion: 
    """

    while True:
        opcion = input(menu)

        if opcion == '1':
            mensaje = """ 
            El reto consiste en realizar 3 sumas seguidas
            para ganar debe conseguir 7 aciertos de 10 
            Mucha Suerte!!!
            """
            print(mensaje)

            nota = aprenderSumar()
            if nota >= 70:
                print("Usted ha superado el reto Felicitaciones !!!")
            else:
                print("Lo sentimos usted ha fallado Intentelo de nuevo")
        elif opcion == '2':
            mensaje = """
            El reto consiste en completar la tabla de multiplicar 
            Solo puede elegir una tabla entre 2 y 12
            Para ganar el Juego debe conseguir al menos 7 aciertos
            """

            print(mensaje)
            tabla = verificarValor(input("Ingrese la tabla de multiplicar deseada: "))
            if 2 <= tabla <= 12:
                nota = aprenderTablasMultiplicar(tabla)
                if nota >= 70:
                    print("Usted ha superado el reto Felicitaciones !!!")
                else:
                    print("Lo sentimos usted ha fallado Intentelo de nuevo")
            else:
                print("Solo se permiten tablas entre 2 y 12")
        elif opcion == '4':
            exit(0)
        else:
            print("La opcion digitada es incorrecta")


#######################################################################################################################
if __name__ == "__main__":
    run()
