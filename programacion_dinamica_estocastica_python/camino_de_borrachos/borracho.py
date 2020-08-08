# borracho.py
""" Clase que representa un caminante borracho. """

import random

class Borracho:
    """ Clase que representa un caminante borracho """
    
    def __init__(self, nombre):
        self.nombre = nombre
        

class BorrachoTradicional(Borracho):
    
    def __init__(self, nombre):
        super().__init__(nombre)
        
    def camina(self):
        #return random.choice([(0,1), (0,-1), (1,0), (-1,0)])
        return random.choice([(0,1), (0,-1), (1,0), (-1,0), (1,1), (-1,1), (1,-1), (-1, -1)])
    