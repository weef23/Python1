def run():
    my_list = [1, "Hello World", True, 4.5]
    mi_dict = {"firstname":"Facundo", "Lastname":"Garcia"}
    ### Diccionarios dentro de las listas regulares
    super_list = [
        {"firstname": "Facundo", "Lastname": "Garcia"},
        {"firstname": "Miguel", "Lastname": "Torres"},
        {"firstname": "Pepe", "Lastname": "Rodelo"},
        {"firstname": "Ron", "Lastname": "Gomez"}
    ]

    super_dic = {
        "naturales" : [1, 2, 3, 4, 5, 6, 7, 8, 9],
        "enteros": [-1,-2,-3,0,1,2,3],
        "decimales" : [1.1, 1.2, 1.3, 1.4]
    }

    ## Impresion de diccionarios usando dic comprehension
    {print(f"Clave: {clave} -> Valor: {valor}") for (clave, valor) in super_dic.items()}

if __name__ == "__main__":
    run()