#### Vamos a crear una funcion que se encarga de validar que el valor sea un numero
def verificarValor(valor):
    if(str.isnumeric(valor)):
        return int(valor)
    else:
        print("Solo es posible convertir valores numericos")
        exit(0)

############## Creamos una funcion que se encargue de la conversion ######################
def conversorMonedad(moneda,valorConversion,operacion=0):
    valor = verificarValor(input(f"Ingrese la cantidad de {moneda} a convertir: "))
    conversion = round(valor * valorConversion)
    print(f"Su conversion es: {conversion}")


## La siguiente es una forma mas elegante de crear un menu usando una cadena de
## Multiples lineas
menu = """
Bienvenido al conversor de monedas 💰💰
1- Convertir de Cordobas a Dolares
2- Convertir de Cordobas a Euros
3- Convertir de Dolares a Cordobas 
4- Convertir de Euros a Cordobas 

Seleccione una opcion por favor: 
"""
## Leemos el valor
opcion = input(menu)

if(opcion == '1'):
    conversorMonedad("cordoba", 0.02777, 0)
elif(opcion == '2'):
    conversorMonedad("cordoba", 0.02833, 0)
elif(opcion == '3'):
    conversorMonedad("dolares", 36, 0)
elif(opcion == '4'):
    conversorMonedad("euro", 35.29, 0)
else:
    print(f"Opcion invalida vuelva a intentarlo.")
