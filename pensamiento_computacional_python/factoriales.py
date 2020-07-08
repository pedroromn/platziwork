#! -*- coding: utf-8 -*-
# Calcula el factorial de n ( entero > 0 )

def factorial(n):
    """Calcula el factorial de n.
    
    n int > 0
    returns n!
    """
    print(n)
    if n == 1:
        return 1
    
    return n * factorial(n -1)


def main():
    n = int(input("Escoge un entero: "))
    print(f"{n}! = {factorial(n)}")
    
    
if __name__ == "__main__":
    main()