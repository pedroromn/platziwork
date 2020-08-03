# cuadrado.py
""" Programa que pinta un cuadrado en la ventana usando el módulo turtle  """
import turtle

def main():
    window = turtle.Screen()
    myturtle = turtle.Turtle()
    myturtle.forward(50)
    myturtle.left(90)
    myturtle.forward(50)
    myturtle.left(90)
    myturtle.forward(50)
    myturtle.left(90)
    myturtle.forward(50)
    myturtle.left(90)
    turtle.mainloop()

if __name__ == "__main__":
    main()
