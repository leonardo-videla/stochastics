# -*- coding: utf-8 -*-
"""
Created on Tue Apr 26 20:59:26 2022

@author: leona
"""
import numpy as np
from random import randrange
import matplotlib.pyplot as plt
from matplotlib import cm
from matplotlib.ticker import LinearLocator
from mpl_toolkits.mplot3d import Axes3D

def Dirichlet_Problem (dataN, dataS, dataE, dataW, NSAMPLES):
    nx=len (dataN)
    ny=len (dataW)
    grid=np.zeros ((nx, ny))
    for i in range (NSAMPLES):
        ix = randrange (nx)
        iy = randrange (ny)
        x=ix
        y=iy
        while x !=-1 and y != -1 and x != nx and y!=ny:
            p=randrange (4)
            if p==0:
                x=x+1
            elif p==1:
                x=x-1
            elif p==2:
                y=y+1
            else:
                y=y-1
        if x==-1:
            grid[ix][iy]=grid[ix][iy]+dataW[y]
        elif x==nx:
            grid [ix][iy]=grid[ix][iy]+dataE[y]
        elif y==0:    
            grid[ix][iy]=grid[ix][iy]+dataN[x]
        else:
            grid[ix][iy]=grid[ix][iy]+dataS[x]
    
    grid=grid/NSAMPLES
    
    X, Y = np.meshgrid(range(nx), range(ny))
    hf, ha  =  plt.subplots(subplot_kw={"projection": "3d"})
   # ha.plot_surface(X, Y, grid, cmap=cm.coolwarm, linewidth=0, antialiased=False)
    ha.plot_surface(X, Y, grid, cmap=cm.coolwarm)
    
    ha.set_zlim(-1.01, 2)
    
    
    ha.zaxis.set_major_locator(LinearLocator(10))
# A StrMethodFormatter is used automatically
    #ha.zaxis.set_major_formatter('{x:.02f}')

    plt.show()

    
    
    
    
   # plt.imshow(grid, cmap='hot', interpolation='nearest')
   # plt.show()
    
    
    
        