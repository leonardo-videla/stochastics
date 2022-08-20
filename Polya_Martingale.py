# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 18:27:42 2021

@author: leona
"""

import samplea as samplea
from matplotlib import pyplot as plt
import numpy as np
def Polya_Martingale (N, T):
 
    data=[]
  
    for d in range (1, N+1):
        b=1
        n=1
        registro2=[]
  
        registro2.append(b)
    
        for i in range(2, T+1):
            j=samplea.samplea ([n/(n+b), b/(n+b)])
            if j==0:
                n=n+1
            else:   
                b=b+1
            registro2.append(b/i);
        plt.plot (np.linspace(1, T, T), registro2)        
        data.append(registro2[T-1])        

    plt.show()
                
    
    plt.figure(figsize=[10,8])
    n, bins, patches = plt.hist(x=data, bins=8, color='#0504aa',alpha=0.7, rwidth=0.85)
    plt.grid(axis='y', alpha=0.75)
    plt.xlabel('Proporcion',fontsize=15)
    plt.ylabel('Frecuencia',fontsize=15)
    plt.xticks(fontsize=15)
    plt.yticks(fontsize=15)
    plt.ylabel('Frecuencia',fontsize=15)
    plt.title('Distribucion asintotica, Urna de Polya',fontsize=15)
    
    plt.show()
