#! -*- coding: utf-8 -*-
# Función en una expresión usando el Keyword lambda

def main():
    #a, b = int(input("Escoge dos enteros: "))
    a, b = map(int, input("Escoger dos enteros: ").split())
    sumar = lambda x, y : x + y
    print(f"{a} + {b} = {sumar(a,b)}")
    
    
if __name__ == "__main__":
    main()