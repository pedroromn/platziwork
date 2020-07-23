# ordenamiento_por_mezcla.py
""" algoritmo de ordenamiento por mezcla ( merge sort ). """
import random

def ordenamiento_por_mezcla(lista):
    if len(lista) > 1:
        medio = len(lista) // 2
        izquierda = lista[:medio]       # izquierda irá desde el índice 0 hasta medio-1
        derecha = lista[medio:]         # derecha irá desde él indice medio hasta el final
        print(izquierda, '*'*5, derecha )
        
        # Llamada recursiva en cada mitad - hasta tener sublistas de un elemento
        ordenamiento_por_mezcla(izquierda)
        ordenamiento_por_mezcla(derecha)
        
        # Iteradores para recorrer las dos sublistas
        i = 0   # iterador de la sublista izquierda
        j = 0   # iterador de la sublista derecha
        # Iterador para recorrer la lista principal (lista)
        k = 0
        
        while i < len(izquierda) and j < len(derecha):
            print(f"izquierda[{i}] < derecha[{j}]: {izquierda[i]} < {derecha[j]}")
            print(f"lista[{k}]: {lista[k]}")
            if izquierda[i] < derecha[j]:
                lista[k] = izquierda[i]
                i += 1
                print('-'*50)
                print("while 1 : condición 1")
                print(f"lista[{k}]: {lista[k]}")
                print('-'*50)
            else:
                lista[k] = derecha[j]
                j += 1
                print('-'*50)
                print("while 1: condición 2")
                print(f"lista[{k}]: {lista[k]}")
                print('-'*50)
            
            k += 1
            print('-'*50)
            print("k += 1")
            print(f"k: {k}")
            print('-'*50)
            
        while i < len(izquierda):
            lista[k] = izquierda[i]
            print(f"lista[{k}]: {lista[k]}")
            i += 1
            k += 1
            print('-'*50)
            print("while 2: i+=1, k+=1")
            print(f"i: {i}, k: {k}")
            print('-'*50)
            
        while j < len(derecha):
            lista[k] = derecha[j]
            print(f"lista[{k}]: {lista[k]}")
            j += 1
            k += 1
            print('-'*50)
            print("while 3: j+=1, k+=1")
            print(f"j: {j}, k: {k}")
            print('-'*50)
            
        print(f"izquierda: {izquierda}, derecha: {derecha}")
        print(lista)
        print('-'*50)
            
    return lista


if __name__ == "__main__":
    tamano_de_lista = int(input("De qué tamaño será la lista?: "))
    lista = [random.randint(0, 100) for value in range(tamano_de_lista)]
    print(lista)
    print('-' * 50)
    lista_ordenada = ordenamiento_por_mezcla(lista)
    print(lista_ordenada)    
