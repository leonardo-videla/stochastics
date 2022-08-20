# -*- coding: utf-8 -*-
"""
Created on Fri Aug 19 10:06:08 2022

@author: leona
"""

import numpy as np
import random as rd
from  matplotlib import pyplot as plt

def SIR (S0, I0, R0, p, q, niter):
    data=[]
    N=S0+I0+R0
    data.append([S0, I0, R0])
    S=S0
    I=I0
    R=R0
    for _ in range (niter-1):
        p1=rd.random()
        s=rd.random()
        if p1 <= I/N:
            if s <= q:
                I=I-1
                R=R+1
        else:
            if p1 > I/N and p1 < (I+S)/N:
                p2=rd.random()
                if s <= p and p2 <=I/N: 
                    S=S-1
                    I=I+1
        data.append([S, I, R])
    return np.transpose (np.array(data))    

def plot_SIR (S0, I0, R0, p, q, niter):
    data=SIR (S0, I0, R0, p, q, niter)
    s=data[0]
    i=data[1]
    r=data[2]
    plt.plot (np.linspace(0, niter, niter), s)
    
    plt.plot (np.linspace(0, niter, niter), i)
    
    plt.plot (np.linspace(0, niter, niter), r)
    plt.show()
    
def plot_scaled_SIR (S0, I0, R0, gam, bet, T):
    N=S0+I0+R0
    dt= (np.minimum ([1/gam], [1/bet]))/(2*N)
    c=N*dt
    p=gam*c
    q=bet*c
    niter=int(np.floor(T/dt))
    data=(1/N)*SIR(S0, I0, R0, p, q, niter)
    s=data[0]
    i=data[1]
    r=data[2]
    plt.plot (np.linspace(0, T, niter), s)
    
    plt.plot (np.linspace(0, T, niter), i)
    
    plt.plot (np.linspace(0, T, niter), r)
    plt.show()
    
    d=[]
    sdet=S0/N
    idet=I0/N
    rdet=R0/N
    d.append([sdet, idet, rdet])
    for j in range(niter-1):
        sdet=sdet- dt*gam*sdet*idet
        idet=idet + dt*idet*(gam*sdet-bet)
        rdet=rdet+dt*bet*idet
        d.append([sdet, idet, rdet])
    dat=np.transpose (np.array(d))
    ss=dat[0]
    ii=dat[1]
    rr=dat[2]
    plt.plot (np.linspace(0, T, niter), ss)
    
    plt.plot (np.linspace(0, T, niter), ii)
    
    plt.plot (np.linspace(0, T, niter), rr)
    plt.show()
    
    
    
        
        
        
        
        
        
        
        
        
    