# turtle_funciones.py
""" Crear un cuadrado creando funciones en Python 3 """
import turtle


def avanzar_girar(tortuga, lado):
    tortuga.forward(lado)
    tortuga.left(90)
    
def pintar_cuadrado(tortuga, lado):
    
    for i in range(4):
        avanzar_girar(tortuga, lado)
        
def main():
    lado = int(input("Elige longitud del lado: "))
    ventana = turtle.Screen()
    tortuga = turtle.Turtle()
    pintar_cuadrado(tortuga, lado)
    turtle.mainloop()
    
if __name__ == "__main__":
    main()