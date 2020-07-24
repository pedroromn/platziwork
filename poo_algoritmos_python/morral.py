# morral.py
""" Estudio del problema del morral. """

def morral(tamano_morral, pesos, valores, n):
    
    # Si ya no hay más elementos para echar al morral (n == 0) o
    # al morral no le cabe más (tamano_morral == 0)
    if n == 0 or tamano_morral == 0:
        return 0
    
    # Si el peso del elemento que voy a echar al morral pesa más de lo
    # que se puede introducir al morral en ese momento.
    if pesos[n - 1] > tamano_morral:
        return morral(tamano_morral, pesos, valores, n - 1)
    
    # Retorno el máximo entre la suma de valores cuando tomo el elemento y lo echo al morrar, y 
    # cuando no lo echo.    
    return max(valores[n - 1] + morral(tamano_morral - pesos[n - 1], pesos, valores, n - 1), 
               morral(tamano_morral, pesos, valores, n - 1))
    
    
if __name__ == "__main__":
    valores = [60, 100, 120]
    pesos = [10, 20, 30]
    tamano_morral = 50 # Peso máximo que soporta el morral
    n = len(valores)
    resultado = morral(tamano_morral, pesos, valores, n)
    print(f"Valor máximo luego de introducir elementos al morral: {resultado}")