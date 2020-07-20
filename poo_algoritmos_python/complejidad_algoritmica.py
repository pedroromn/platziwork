# complejidad_algoritmica.py
""" Módulo en el que se compara la complejidad temporal entre un algoritmo iterativo y uno 
recursivo para caulcular el factorial de un número entero mayor que cero. """
#import sys
import time

def factorial(n):
    respuesta = 1
    while n > 1:
        respuesta *= n
        n -= 1
    
    return respuesta

def factorial_recursivo(n):
    if n == 1:
        return 1
    
    return n * factorial_recursivo(n - 1)
    

def main():
    #sys.settrace
    #sys.setrecursionlimit(1000000)
    n = 100
    tiempo_inicial_fact = time.time()
    factorial(n)
    tiempo_final_fact = time.time()
    delta_t_fact = tiempo_final_fact - tiempo_inicial_fact
    print(f"delta_t_fact: {delta_t_fact}")
    
    tiempo_inicial_factr = time.time()
    factorial_recursivo(n)
    tiempo_final_factr =time.time()
    delta_t_factr = tiempo_final_factr - tiempo_inicial_factr
    print(f"delta_t_factr: {delta_t_factr}")
    
    delta_t = abs(delta_t_fact - delta_t_fact)
    print(f"|delta_t|: {delta_t}")
    
if __name__ == "__main__":
    main()