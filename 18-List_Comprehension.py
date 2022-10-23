########################### LIST COMPREHESION ############################################################
import random

numbers = []

### Generando una lista vacia y rellenandola con numeros de 1 al 10
for element in range(1, 10):
    numbers.append(element)
### Esto mismo lo podemos hacer de la siguiente forma con menos lineas de codigo
numbers_v2 = [element for element in range(1, 10)]

print(numbers)
print(numbers_v2)
#######################################################################################################
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

## Usando list comprehesion traemos los dias que tengan la letra a

dias_letra_a = [i for i in dias if 'a' in i]
print(dias_letra_a)
### La sintaxis para la list comprehension es elemento + ciclo + condicion

### Lista de numeros pares
pares = [i * 2 for i in range(1, 100) if i % 2 == 0]
print(pares)
## Lista de numeros impares
impares = [(i * 2) + 1 for i in range(1, 100) if i % 2 != 0]
print(impares)

####### Tambien podemos usar el mismo principio de list comprenhesion a los diccionario
#### Sintaxis clave:valor + Ciclo + condicion

nombre = ["Carlos", "Pedro", "Juan"]
edad = [21, 18, 22]

## Siguiente ejemplo crea un diccionario a partir de dos listas un ejemplo muy util
diccionario = {nombre[i]: edad[i] for i in range(len(nombre))}

### Otro Ejemplo de dictionary comprenhension
paises = ['MEX', 'GUA', 'SAL', 'HON', 'NI']

poblacion = {pais: random.randint(1, 1000) for pais in paises}
print(poblacion)

### La funcion zip nos permite unir dos listas pero en forma de tuplas

### Con esto tambie podemos ingresas en un diccionario dos listas
nuevo_dic = {nombre: edad for (nombre, edad) in zip(nombre, edad)}
print(nuevo_dic)

#### Uso de condicionales en la creacion de diccionarios

poblacion_densa = {pais: poblacion for (pais, poblacion) in poblacion.items() if poblacion > 400}
print(poblacion_densa)