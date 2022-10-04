###### Creamos un conversor de monedas sencillo con Python
valor = input("Ingrese el valor a  convertir: ")

### Validamos que el valor introducido sea un numero utilizado
### la funcion is numeric de la clase String
if(str.isnumeric(valor)):
    valor = float(valor) ## Convertimos el valor a decimal.
else:
    ## Si el valor no es correcto te sacara del programa.
    print("El valor introducido no es valido ")
    exit()

### Vamos a seleccionar la moneda a la que deseamos convertir
opcion = input("Seleccione la Moneda a la que desea convertir \n"
               "1- Cordobas a Dolares\n"
               "2- Cordobas a Euros\n"
               "3- Dolares a Cordobas\n"
               "4- Dolares a Cordobas\n")

### Ejecutamos la conversion y devolvemos el resultado
if(opcion == '1'):
    conversion = round(valor/36, 2) ## conversion a dolares
    print(f"Su conversion a dolares es: {conversion}")
elif(opcion == '2'):
    conversion = round(valor/35.29, 2) ### Conversion a Euros
    print(f"Su conversion a euros es: {conversion}")
elif(opcion == '3'):
    conversion = round(valor * 36, 2)  ## conversion a dolares
    print(f"Su conversion a cordobas es: {conversion}")
elif(opcion == '4'):
    conversion = round(valor * 35.29, 2)  ### Conversion a Euros
    print(f"Su conversion a cordobas es: {conversion}")
else:
    print("opcion equivocada")

