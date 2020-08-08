# camino_aleatorio.py
""" Implementación de la simulación, haciendo que el borracho camine por el campo """

from borracho import BorrachoTradicional
from coordenada import Coordenada
from campo import Campo
from bokeh.plotting import figure, show


def caminata(campo, borracho, pasos):
    inicio = campo.obtener_coordenada(borracho)
    
    for _ in range(pasos):
        campo.mover_borracho(borracho)
        
    return inicio.distancia(campo.obtener_coordenada(borracho))


def simular_caminata(pasos, numero_de_intentos, tipo_de_borracho):
    borracho = tipo_de_borracho(nombre='David')
    origen = Coordenada(0, 0)
    distancias = []
    
    for _ in range(numero_de_intentos):
        campo = Campo()
        campo.agregar_borracho(borracho, origen)
        simulacion_caminata = caminata(campo, borracho, pasos)
        distancias.append(round(simulacion_caminata, 1))
        
    return distancias

def graficar(x, y):
    grafica = figure(title='Camino Aleatorio del Borracho', x_axis_label='pasos', y_axis_label='distancia')
    
    # Ingresamos los datos de x e y.
    grafica.line(x, y, legend_label='distancia media')
    
    # se genera una gráfica en Html
    show(grafica)

       
def simulacion_borracho(distancias_caminata, numero_intentos, tipo_de_borracho):
    
    # Se crea una lista que guarde la distancia media por cada caminata
    distancias_media_por_caminata = []
    
    for pasos in distancias_caminata:
        distancias = simular_caminata(pasos, numero_intentos, tipo_de_borracho)
        distancia_media = round(sum(distancias) / len(distancias), 4)
        distancia_maxima = max(distancias)
        distancia_minima = min(distancias)
        print(f'{tipo_de_borracho.__name__} tuvo caminata aleatoria de {pasos} pasos')
        print(f'Media = {distancia_media}')
        print(f'Max = {distancia_maxima}')
        print(f'Min = {distancia_minima}')
        distancias_media_por_caminata.append(distancia_media)
    
    # Gráfica: Pasos vs Distancias medias por caminata    
    graficar(distancias_caminata, distancias_media_por_caminata)


def main():
    distancias_de_caminata = [10, 100, 1000] #, 10000, 100000, 1000000]
    numero_de_intentos = 100
    simulacion_borracho(distancias_de_caminata, numero_de_intentos, BorrachoTradicional)


if __name__ == "__main__":
    main()