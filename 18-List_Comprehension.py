########################### LIST COMPREHESION ############################################################
numbers = []

### Generando una lista vacia y rellenandola con numeros de 1 al 10
for element in range(1,10):
    numbers.append(element)
### Esto mismo lo podemos hacer de la siguiente forma con menos lineas de codigo
numbers_v2 = [element for element in range(1,10)]

print(numbers)
print(numbers_v2)

#######################################################################################################
dias = ["lunes", "martes", "miercoles", "jueves", "viernes", "sabado", "domingo"]

## Usando list comprehesion traemos los dias que tengan la letra a

dias_letra_a = [i for i in dias if 'a' in i]
print(dias_letra_a)
### La sintaxis para la list comprehension es elemento + ciclo + condicion

### Lista de numeros pares
pares = [i*2 for i in range(1, 100) if i % 2 == 0]
print(pares)
## Lista de numeros impares
impares = [(i*2)+1 for i in range(1, 100) if i % 2 !=0]
print(impares)