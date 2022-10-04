###### Este es un ejemplo de como mejorar el conversor usando condicionales
#### Vamos a crear una funcion que se encarga de validar que el valor sea un numero
def verificarValor(valor):
    if(str.isnumeric(valor)):
        return int(valor)
    else:
        print("Solo es posible convertir valores numericos")
        exit(0)

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
    valor = verificarValor(input("Ingrese la cantidad de cordobas a convertir: "))
    conversion = round(valor / 36, 2)  ## conversion a dolares
    print(f"Su conversion a dolares es: {conversion}")
elif(opcion == '2'):
    valor = verificarValor(input("Ingrese la cantidad de cordobas a convertir: "))
    conversion = round(valor / 35.29, 2)  ### Conversion a Euros
    print(f"Su conversion a euros es: {conversion}")
elif(opcion == '3'):
    valor = verificarValor(input("Ingrese la cantidad de dolares a convertir: "))
    conversion = round(valor * 36, 2)  ## Dolares a cordobas
    print(f"Su conversion a cordobas es: {conversion}")
elif(opcion == '4'):
    valor = verificarValor(input("Ingrese la cantidad de euros a convertir: "))
    conversion = round(valor * 35.29, 2)  ### Conversion a Euros
    print(f"Su conversion a cordobas es: {conversion}")
else:
    print(f"Opcion invalida vuelva a intentarlo.")