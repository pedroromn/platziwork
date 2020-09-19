# calculo_pi.py
""" Cálculo del número Pi usando simulación de montecarlo. """
import random
import math
from estadisticas import media, varianza, desviacion_estandar

def aventar_agujas(numero_de_agujas):
    adentro_del_circulo = 0
    
    for _ in range(numero_de_agujas):
        x = random.random() * random.choice([-1, 1])
        y = random.random() * random.choice([-1, 1])
        distancia = math.sqrt(x**2 + y**2)      # distancia desde el centro del círculo
        
        if distancia <= 1:
            adentro_del_circulo += 1
            
    return (4 * adentro_del_circulo) / numero_de_agujas

def estimacion(numero_de_agujas, numero_de_intentos):
    estimados = []          # estimaciones del número Pi    
    for _ in range(numero_de_intentos):
        estimacion_pi = aventar_agujas(numero_de_agujas)
        estimados.append(estimacion_pi)
    
    media_estimados = media(estimados)
    varianza_estimados = varianza(estimados, media_estimados)
    sigma = desviacion_estandar(varianza_estimados)
    print(f"Estimado: {media_estimados:.5f} - sigma: {sigma:.5f}")
    
    return (media_estimados, sigma)
    
def estimar_pi(precision, numero_de_intentos):
    numero_de_agujas = 1000
    sigma = precision
    
    while sigma >= precision / 1.96:
        media, sigma = estimacion(numero_de_agujas, numero_de_intentos)
        numero_de_agujas *= 2
        
    return media

if __name__ == "__main__":
    estimar_pi(0.01, 1000)
            
        