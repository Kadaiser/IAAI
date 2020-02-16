import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from pandas.io.parsers import read_csv
from matplotlib.ticker import LinearLocator, FormatStrFormatter
from pprint import pprint

def coste(x, y, a, b):
    m = len(x)
    error = 0.0
    for i in range(m):
        hipotesis = a+b*x[i]
        error +=  (y[i] - hipotesis) ** 2
    return error / (2*m)

def descenso_gradiente(x, y, a, b, alpha, iterations):
    m = len(x)
    hist_coste = []
    for i in range(iterations):
        b_deriv = 0
        a_deriv = 0
        for i in range(m):
            hipotesis = a+b*x[i]
            a_deriv += hipotesis - y[i]
            b_deriv += (hipotesis - y[i]) * x[i]
            hist_coste.append(coste(x, y, a, b))
        a -= (a_deriv / m) * alpha
        b -= (b_deriv / m) * alpha
        
    return a, b, hist_coste


def carga_csv(fileName):
    valores =  read_csv(fileName, header=None).values
    return valores.astype(float)

if __name__ == "__main__":
    datos = carga_csv('C:\\Users\\valbu\\Desktop\\IAAI\\Practica1\\ex1data1.csv')
    #pprint(datos)

    X = datos[:, :-1]
    Y = datos[:, -1]
    
    a = 1
    b = 1
    alpha = 0.01
    iterations = 1500

    a,b, hist_coste = descenso_gradiente(X, Y, a, b, alpha, iterations)
        
    
    x = np.linspace(min(X),max(X),100)
    y = b*x+a

    plt.figure()
    plt.scatter(X, Y, color='red', marker="x")
    plt.plot(x, y, '-', color="blue")
    plt.show()