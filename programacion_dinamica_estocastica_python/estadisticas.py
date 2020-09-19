# estadisticas.py
import random
import math

def media(X):
    """ Calcula la media de un conjunto de datos X. """
    return sum(X) / len(X)

def varianza(X, mu):
    """ Calcula la varianza de un conjunto de datos X, con media mu."""
    acumulador = 0
    for x in X:
        acumulador += (x - mu)**2
        
    return acumulador / len(X)

def desviacion_estandar(var):
    """ Calcula la desviación estandar (sigma) de un conjunto de datos. """
    return math.sqrt(var) # var: varianza del conjunto de datos

if __name__ == "__main__":
    X = [random.randint(1,51) for i in range(21)]
    mu = media(X)
    print("Datos: ", sep=' ')
    print(X)
    print(f"Media (mu): {mu:.2f}")
    var = varianza(X,mu)
    print(f"Varianza (var): {var:.2f}")
    print(f"Desviación Estandar(sigma): {desviacion_estandar(var):.2f}")