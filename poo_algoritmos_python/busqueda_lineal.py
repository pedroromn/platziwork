# busqueda_lineal.py
""" Algoritmo de búsqueda lineal  """

import random

def busqueda_lineal(lista, objetivo):
    match = False

    for elemento in lista:          # O(n)
        if elemento == objetivo:
            match = True
            break
    
    return match


if __name__ == "__main__":
    tamano_de_lista = int(input("De qué tamaño será la lista?: "))
    objetivo = int(input("Número que quieres buscar: "))
    
    lista = [random.randint(0, 100) for value in range(tamano_de_lista)]
    print(lista)
    encontrado = busqueda_lineal(lista, objetivo)
    print(f"El elemento {objetivo} {'está' if encontrado else 'no está'} en la lista")
    