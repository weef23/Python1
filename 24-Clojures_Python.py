############################ Clojures en Python ##############################################
############ Las Funciones CLojures son funciones que a su vez encapsulan mas funciones ######
####### Un Closure es defina otra funcion y la puede regresar ################################

### La funcion operacion define a la funcion principal
def operacion(a, b):
    ### Internamente definimos la funcion sumar
    def sumar():
        return  a + b

    ## Retornamos la funcion como tal

    return sumar ## No es necesario poner parentesis

## Tambien podemos  hacer lo mismo usando funciones lambda
def operacion_lambda(a, b):
    return lambda : a + b ## es similar a la anterior pero con menos codigo

mi_operacion = operacion(5, 3)

### Cuando nosotros llamamos a la funcion principal
## Inmediatamente esta nos regresa el resultado de la funcion interior

print(f"El valor de la operacion es {mi_operacion()}")

### Otra forma es invocando a la misma funcion y luego a la funcion interna
print(f"El valor de la operacion es {operacion(5, 6)()}")
### Python tiene la particularidad que para el todo es un objeto
print(f"El valor de la operacion es {operacion_lambda(6, 6)()}")