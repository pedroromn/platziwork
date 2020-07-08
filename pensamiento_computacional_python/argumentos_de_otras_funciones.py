#! -*- coding: utf-8 -*-
# Paso de funciones como argumentos de otras funciones

def multiplicar_por_dos(n):
    return n * 2

def sumar_dos(n):
    return n + 2

def aplicar_operacion(funcion, numeros):
    resultados = []
    if isinstance(numeros, list):
        for numero in numeros:
            resultados.append(funcion(numero))
        
        return resultados
    else:
        print("Debes pasar una lista como parámetro")
        
def main():
    numeros = [1,2,3,4,5]
    resultados = aplicar_operacion(multiplicar_por_dos, numeros)
    print(resultados, sep=' ')
    
    
if __name__ == "__main__":
    main()
