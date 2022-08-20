# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 20:49:49 2021


"""


from matplotlib import pyplot as plt
import numpy as np


def samplea (prob):
    n=len(prob)
    suma=[prob[0]]
    for i in range (1,n):
        suma.append(suma[i-1]+prob[i])
    i=0
    p = np.random.rand()
    while p> suma[i]:
        i=i+1
    return i


def transporta(A, pesos_iniciales, n_iter):
    l=len(A)
    prob=[]
    for i in range(l):
        for j in range(l):
            prob.append (A[i][j])
    dat=[]
    dat.append(pesos_iniciales)
    n=1
    while n < n_iter:
        k=samplea (prob)
        i=np.int( np.floor (k/l))
        j=k-i*l
        U=np.random.rand() 
        p=np.random.rand()
        D=[element for element in dat[n-1]]
        if p < 1/2:
            T=D[i]
            D[i]=T*U
            D[j]= D[j]+T*(1-U) 
        else:
            T=D[j]
            D[j]=T*U
            D[i]= D[i]+T*(1-U) 
        dat.append(D)
        n=n+1
    return dat

def muestra_evol_promedios (A, pesos, n_iter, nsamples):
    
    datos=np.zeros((n_iter, len(A)))
    l=len(A)
    for i in range (nsamples):
        print("Comenzando iteracion: ")
        D=transporta(A, pesos, n_iter)
        datos=np.add(datos, D)
    
    datos=datos/nsamples 
    datos=np.transpose(datos)
    x=np.linspace (0, n_iter, n_iter)
  

    G=np.array(A)
    s=list(sum (np.transpose(G)))
    r= np.diag(s)
    G=G-r
    print(G)
    y=np.zeros((n_iter, l) )
    y[0]=pesos
    for i in range(1,n_iter):
        y[i]=y[i-1] + (1/2)*y[i-1].dot (G) 
    y=np.transpose(y)
    for k in range (len(A)):
        plt.subplot (len(A)+1, 1, k+1)
        plt.plot (x, datos[k], 'b-')
        plt.plot (x, y[k], 'r--')
        plt.xlabel('iteration')
        plt.ylabel('average') 
        plt.show()
    
    
    
    



