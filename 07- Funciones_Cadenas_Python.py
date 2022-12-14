######################## Cadenas de Caracteres ################################
## Metodos utiles para manipulacion de cadenas de caracteres
nombre = "jose maria"
## Python todo es un objeto eso incluye las cadenas de caracteres
## para invocar los metodos de manipulacion de cadenas invocamos a la clase str
### CONVERTIR TODA LA Cadena en mayuscula
print(str.upper(nombre))
cadena2= "ESTO ES UNA CADENA"
## Convierte una cadena en minuscula
print(str.lower(cadena2))
#############################################################################
## Pone la primera letra en mayusculas
print(str.capitalize(nombre))

### las variables de tipo cadena de caracter tambien heredan los metodos de la
## Clase string y pueden invocarse de la siguiente manera

print(nombre.upper())
print(cadena2.lower())
## Elimina espacios en blanco
print(cadena2.strip())
## Remplazar un caracter por otro
print(cadena2.replace ('A', '@'))

## Las cadenas de caracteres tambien son arreglos de caracteres
## lo que nos permite usar los indices para obtener cada letra

print(nombre[0])  ## Me devuelve la primera letra
## Al ser un arreglo yo puedo usar los indices para obtener pedazos de la cadena
print(nombre[0:3]) ## Cuatro primeros caracteres
print(nombre[2:4]) ## Del indice 2 al 4
print(nombre[1:7:2]) ## El 2 representa el numero de pasos
## Devuelve la cadena alreves
print(nombre[::-1])
## La funcion len me da la logitud de caractes
print(len(cadena2))

### La siguiente funcion nos ayuda a buscar la posicion de un caracter especifico
#### Funcion find para buscar cadenas de caracteres.
print(cadena2.find('A'))
### Funcion rfind busca el ultima letra
print(cadena2.rfind('A'))
#Anteriormente vimos la funcion lower para convertir una cadena en mayusculas
## Sin embargo existe una funcion llamada islower que permite veridicar si una cadena esta o no en minusculas
cadena_minunscula = "esta cadena esta en minuscula"
print(cadena_minunscula.islower()) ## Nos regresa True.
## Tambien podemos validar si una cadena esta toda en mayusculas
print(cadena_minunscula.isupper()) ## Nos retorna False
