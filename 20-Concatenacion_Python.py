########################## CONCATENACION EN PYTHON ####################################################
## Aunque es un tema sencillo es algo que es muy utilizado, concatenar caracteres en python
#######################################################################################################
numero_entero = 5

## La forma mas sencilla de hacerlo es la siguiente
print("Esto es un numero entero",numero_entero)

###Tambien podemos usar %i para indicar a python que lo que concatenamos
###Es un entero, esto lo hacemos de la siguiente forma
print("Esto es un entero %i"%(numero_entero))

## Podemos usar la clase str para convertir el entero en un string
## Una forma poco elegante pero valida
print("Esto es un entero " + str(numero_entero))
#####################################################################################################
### La que usamos mayoritariamente en todo el curso

print(f"Esto es un entero {numero_entero}")

numero_flotante = 3.14159
##Con los flotantes ocurre exactamente lo mismo
print("Esto es un flotante", numero_flotante)
### Podemos usar el %f para indicarle a Python que estos es un flotante.
print("Esto es un flotante %f"%(numero_flotante))
### Esta forma es interesante porque podemos indicar el numero de decimales
### que deseamos utilizar solo usamos lo siguietes %.nf donde n es
## El numero de decimales que deseamos utilizar.
print("Esto es un numero flotante %.2f"%(numero_flotante))

## Algo muy interesante es end dentro del print
print("Tu nombre es ", end="")
## Con el end si nosotros ejecutamos otro print no se ejecutara un salto de linea
## Se integrara a la linea escrita anteriormente, estos son trucos muy interesantes.
print("Hola mundo")
