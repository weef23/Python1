############# Ejemplo de flujos condicionales en python ####################
## Convertimos edad de string a integer, tambien es posible hacerlo en una sola linea

edad = int(input("Escribe aqui tu edad: "))

####################################################################################
if(edad > 17): ## Si esta por encima de 17 imprimimos eres mayor de edad
    print(f"Eres mayor de edad")
elif (edad > 0 and edad <= 17): ## Si es menor igual que 17 pero mayor que cero es menor de edad
    print(f"Eres menor de edad")
else: ## Si no cumple las condiciones anteriores es un numero negativo
    print(f"No se admiten numeros negativos")
