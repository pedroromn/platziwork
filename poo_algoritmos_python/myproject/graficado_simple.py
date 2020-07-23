# graficado_simple.py
""" Práctica del módulo bokeh para graficar. """
import random
from bokeh.plotting import figure, output_file, show

if __name__ == "__main__":
    output_file('graficado_simple.html')
    fig = figure()
    
    total_vals = int(input("Cuantos valores quieres graficar?: "))
    x_vals = list(range(total_vals))
    #y_vals = [random.randint(0,100) for x in x_vals]
    y_vals = [x**3 for x in x_vals]
    
    #for x in x_vals:
    #val = int(input("Valor y para {" + str(x) + "} : "))
    #y_vals.append(val)
        
    fig.line(x_vals, y_vals, line_width=2)
    show(fig)

