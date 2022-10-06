import random

def verificarValor(valor):
    if(str.isnumeric(valor)):
        return int(valor)
    else:
        print("Solo es posible convertir valores numericos")
        exit(0)
############################Funcion Aprende a sumar#####################################################################
def aprenderSumar():
    a = random.randint(1, 100)
    b = random.randint(1, 100)
    contador = 0
    for i in range(1,10):
        resultado = verificarValor(input(f"Digite el resultado de la suma de {a} + {b} :"))
        if (a + b) == resultado:
            contador+=1
    return (contador/10)*100

##################### Tablas de Multiplicar #################################################################
def aprenderTablasMultiplicar(tabla):
    contador = 0
    for i in range(1,10):
        resultado = verificarValor(input(f"Digite el resultado de multiplicar {i} * {tabla}"))

        if resultado== (i*tabla):
            contador+=1
    return  (contador/10)*100

def run():
    pass

if __name__ == "__main__":
    run()