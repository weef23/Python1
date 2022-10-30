######################### Listas en Python ####################################
### Las listas son un tipo de contenedor que permite almacenar
### Un conjunto de valores.
#### La siguientes operaciones se concideran inmutables porque alteran la definicion de la lista

lista = []  ## Lista vacia
mylista = list()  ## Crea una lista vacia, en python todo es un objeto.

print(type(lista))  ## Podemos ver que es una Objeto tipo lista

lista = ['hola', 2, 3, True]  ## En realidad en este caso la lista convirtio todo a Objeto

### Operaciones con listas
### Apend añade un elemento al final de la lista
lista.append([1, 2])
print(lista)
mylista.append(1)
print(mylista)

## Insert Añade un elemento en una posicion determinada
lista.insert(3, 'y')
print(lista)
mylista.insert(0, 3)
print(lista)

## Extend añade otra lista al final de la lista
lista.extend(mylista)
print(lista)

## Del elimina un elemento en un indice dado
del lista[-1]  ## Elimina el ultimo elemnteo
del lista[2]  ## Elimina el elemento en la posicion 2
print(lista)

### Remove nos permite eliminar la primer coicidencia de la lista
lista.remove('y')  ## Elimina el elemento y
print(lista)

################## Operaciones de Ordenacion ####################################
### Estas operaciones se consideran inmutable porque no alteran la definicion de la lista.

### Sorted nos devuelve la lista de forma ordenada
print(sorted(mylista))  ## Puede generar error cuando tenemos elementos de distintos tipos
## Tambien podemos usar el metodo sort
print("lista invertida ",end="")
lista_invertida = [1,2,3,4,5,6,7,8,9]
## Invertimos la lista
lista_invertida.sort(reverse=True)
print(lista_invertida)

### El operador + nos permite concatenar dos listas
lista2 = lista + mylista
print(lista)
print(mylista)
print(lista2)  ## Lista concatenada
## El operador * nos permite replicar una lista un numero n de veces
print(mylista * 6)
######################## Tuplas en Python ###########################################
### Las Tuplas son un tipo de coleccion muy similar a las tuplas pero con la diferencia
### Que las listas son dinamicas, las tuplas son colecciones que no se pueden modificar
## Lo que las hace mas eficiente cuando tienes elementos que necesitas que no se modifiquen.
## No podemos agregar elementos ni eliminarlos
## Es mucho mas rapido recorrer una tupla con un for que con una lista.
### Ejemplo de una Tupla
tupla1 = (1, 2, 3, 4, 5, 6)
mi_tupla = (1, 2, 3)
mi_otra_tupla = (4, 5, 6)
########## Reasignacion de tuplas
mi_tupla=mi_tupla + mi_otra_tupla
print(mi_tupla)
################################################################################################
################### Un ejemplo de if inline bastante interesante
lista = [1, 2, 5, 25, 33, 56, 75, 21, 56, 89, 43, 13, 62, 24]
### Verificamos si el 21 esta en la lista, una forma elegante de expresar un condicional
### En una sola linea
print("Esta en la lista") if 21 in lista else print("No esta en la lista")
###################################################################################################
tupla = ('Juan', 'Antonio', 'Pedro', 'Maria')

dato = input("Digite el dato que desea buscar: ")

### La misma forma elegante pero para las tuplas
print("Si esta en la tupla") if dato in tupla else print("No esta en la tupla")