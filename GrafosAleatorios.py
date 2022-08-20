""" Clase Grafo
"""
from Grafos import Grafo
import random

def UniformAttachment (n,m, q):
    g=Grafo()
    for i in range(1,m):
        for j in range(i+1, m+1):
            g.agrega_arista(i,j)
    for k in range(m+1, n+1):
        for _ in range(q):
            g.agrega_arista(k, random.randrange(1, k))
    return g

def ErdosRenyi (n,p):
    g=Grafo()
    for k in range(1, n+1):
        g.agrega_vertice(k)
    for i in range(1,n):
        for j in range(i+1, n+1):
            if random.random()< p:
                g.agrega_arista(i,j)
    return g
