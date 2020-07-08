#! -*- coding: utf-8 -*-
# Calcula el término n de la secuencia de fibonacci

def fibonacci(n):
    """Calcula Calcula el término n de la secuencia de fibonacci.
    
    n int > 0
    returns fibonacci(n)
    """
    #print(n)
    if n == 0 or n == 1:
        return 1
    
    return fibonacci(n -1 ) + fibonacci(n - 2)


def main():
    n = int(input("Escoge un entero: "))
    print(f"El término {n} de la secuencia de Fibonacci es {fibonacci(n)}")
    
    
if __name__ == "__main__":
    main()