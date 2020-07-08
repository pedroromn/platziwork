#! -*- coding: utf-8 -*-
# Funciones como elementos de estructuras de datos propias de python

def aplicar_operaciones(num):
    operaciones = [abs, float, chr]
    resultados = []
    
    for operacion in operaciones:
        resultados.append(operacion(num))
        
    return resultados

def main():
    numero = int(input("Escoger un entero: "))
    resultados = aplicar_operaciones(numero)
    print(resultados, sep=' ')
    
if __name__ == "__main__":
    main()