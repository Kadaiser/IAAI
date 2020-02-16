import numpy as np
import matplotlib.pyplot as plt
import time
def funcion_linear(x):
    return x

def funcion_exponencial(x):
    return x**2

#Aproximación de una integral defina f(x) entre a y b con puntos aleatorios
def integra_mc(func, a, b, num_puntos):
    tic = time.process_time()
    x= np.arange(a, b, 0.01)
    y = func(x)
    M = max(y)
    #Generar los puntos aleatorios
    generadosX = a + np.random.random(num_puntos) * (b-a)
    generadosY = 0 + np.random.random(num_puntos)*M

    #Calcular que puntos quedan por encima y por debajo
    #Numpy ofrece operaciones de condicionales con la función where
    #que evalua todos los indices de un array en una unica operación
    debajo = np.where(generadosY < func(generadosX))
    encima = np.where(generadosY >= func(generadosX))

    #Calculo de I
    I = M*(b-a)*len(debajo[0])/num_puntos
    
    toc = time.process_time()
    print (1000 * (toc -tic))

    plt.scatter(generadosX[encima], generadosY[encima], color = "blue")
    plt.scatter(generadosX[debajo], generadosY[debajo], color = "red")
    plt.plot(x,y, color= "black")
    plt.plot(0,0, label='I = {:4.4f}'.format(I))
    plt.legend()
    plt.show()

if __name__ == "__main__":
    num_puntos = 1000
    a = 0
    b = 1
    integra_mc(funcion_exponencial, a, b, num_puntos)