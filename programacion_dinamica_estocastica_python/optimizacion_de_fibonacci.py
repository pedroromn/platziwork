# optimizacion_de_fibonacci.py
""" Técnicas para optimizar el cálculo del número de fibonacci empleando memoization. """
import sys


def fibonacci_no_optimizado(n):
    if n == 0 or n == 1:
        return 1
    
    return fibonacci_no_optimizado(n - 1) + fibonacci_no_optimizado(n - 2)


def fibonacci_optimizado(n, memo = {}):
    if n == 0 or n == 1:
        print('-'*50)
        print(f"n: {n}")
        print("return 1")
        print('-'*50)
        return 1
    
    try:
        print('-'*50)
        print(f"n: {n}")
        print(f"return memo[{n}]: {memo[n]}")
        print('-'*50)
        return memo[n]
    except KeyError:
        resultado = fibonacci_optimizado(n - 1, memo) + fibonacci_optimizado(n - 2, memo)
        print('-'*50)
        print(f"memo[{n}] <= {resultado}")
        print('-'*50)
        memo[n] = resultado
        
        return resultado
    

if __name__ == "__main__":
    #sys.setrecursionlimit(10002)
    n = 10
    resultado = fibonacci_optimizado(n)
    print('-'*50 + '\n')
    print(f"resultado de fibonacci optimizado: {resultado}")