# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import numpy as np
from matplotlib import pyplot as plt

def Lotka_Volterra(b1, b2, a1, a2, x0, y0, h, T, sigma1, sigma2):
    n=int(np.floor(T/h))
    x=[x0]
    y=[y0]
    for i in range (n-1):
        x.append(max(0,x[i]+x[i]*h*(-b1+a1*y[i])+ sigma1*x[i]*np.sqrt(h)*np.random.normal()))
        y.append(max(0,y[i]+y[i]*h*(b2-a2*x[i])+ sigma2*y[i]*np.sqrt(h)*np.random.normal()))
        
    plt.plot (np.linspace(0, T, n), x)
    plt.title("Dinámica de la especie predador")
    plt.xlabel("Tiempo")
    plt.ylabel("Abundancia")
    plt.show()

    plt.plot (np.linspace(0, T, n), y)
    plt.title("Dinámica de la especie presa")
    plt.xlabel("Tiempo")
    plt.ylabel("Abundancia")
    plt.show()
    
    plt.plot (x, y)
    plt.title("Espacio de fase de las abundancias")
    plt.xlabel("Abundancia de especie predador")
    plt.ylabel("Abundancia de especie presa")
    plt.show()
    

 