########## En Python los tipos de datos son objetos #####################
### Para definir una variable en Python simplemente lo hacemos de la siguiente forma
### Ejecuto un cambio para probar el repositorio
x = 4 ## Entero
y = 4.0 ## Decimal
nombre = "Facundo"

## Las variables en python no requieren declaracion de tipo como en el caso de C, C++ o Java.
# z = nombre + y Esto es incorrecto no podemos sumra string con numeros
z= x+y ## Esto si es posible tomara el tipo de mayor jerarquia en este caso decimal
print(z)
### Conversion de tipos de datos
### Valores de entrada
numero = input("Escribe un numero: ")
numero2 = input("Escribe un numero: ")
### Siempre es importante y muy util validar que es lo que estamos ingresando
### La siguiente funcion permite conprobar si lo que ingresamos es o no un numero2.
print(str.isnumeric(numero)) ## Devolvera True si es un numero, false si no lo es
print(str.isnumeric(numero2)) ## Develvera True si es numero, False si no lo es.

### Los valores ingresados anteriormente son valores de cadenas de caracteres
## Tenemos que convertirlo

numero= int(numero) ## Lo convierte en un entero
numero2 = float(numero2) ## Lo convierte en coma flotante

resultado = numero + numero2
print(resultado)

## Tipos de datos Logicos y sus Operadores

estudiante = True
trabaja = False

### Comparadores logicos
## And corresponde al operador logico y devolvera verdadero si ambos son verdaderos
print(estudiante and trabaja) ### Devolvera falso

## Or corresponde al operador o devolvera verdadero si uno solo es verdadero
print(estudiante or trabaja) ## Devolvera verdadero

## Existe tambien el operador de negacion que invierte el valor logico de una variable.

print(not trabaja) ## Invierte el valor trabaja y devuelve true
print(not estudiante) ## Invierte el valor de estudiante y devuelve false

######## Comparadores

print(numero == numero2) ## Comparador igual
print(numero < numero2) ## comparador menor que
print(numero > numero2) ## comparador mayor que
print(numero <= numero2) ## comparador menor igual que
print(numero >= numero2) ## comparador mayor igual que