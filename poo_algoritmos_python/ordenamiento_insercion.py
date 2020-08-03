# ordenamiento_insercion.py
""" Algoritmo de ordenamiento por inserción """
import random

def ordenamiento_insercion(lista):
    for indice in range(1, len(lista)):
        valor_actual = lista[indice]
        print('+'*50)
        print("Inicio del ciclo for")
        print(f"valor_actual <= lista[indice] : valor_actual <= {lista[indice]}")
        posicion_actual = indice
        print(f"posicion_actual <= indice : posicion_actual <= {indice}")
        
        while posicion_actual > 0 and lista[posicion_actual-1] > valor_actual:
            print('+'*50)
            print("Dentro del ciclo while")
            lista[posicion_actual] = lista[posicion_actual-1]
            print('+'*50)
            print(f"lista[posicion_actual] <= lista[posicion_actual-1] : lista[{posicion_actual}] <= {lista[posicion_actual-1]}")
            posicion_actual -= 1
            print(f"posicion_actual -= 1 : posicion_actual: {posicion_actual}")
            
        lista[posicion_actual] = valor_actual
        print('+'*50)
        print("Fuera del ciclo while")
        print(f"lista[posicion_actual] <= valor_actual : lista[{posicion_actual}] <= {valor_actual}")
        
    return lista
        
if __name__ == "__main__":
    tamano_de_lista = int(input("De qué tamaño será la lista?: "))
    lista = [random.randint(0, 100) for value in range(tamano_de_lista)]
    print(lista)
    lista_ordenada = ordenamiento_insercion(lista)
    print(lista_ordenada)    
