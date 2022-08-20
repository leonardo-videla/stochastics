# -*- coding: utf-8 -*-
"""
Created on Tue Jun  1 20:39:51 2021

@author: leonardo
"""

import samplea as samplea
from matplotlib import pyplot as plt
import numpy as np



def Pref_Attachment_Martingale (N, T, jota):
    data=[]
  
    for d in range (1, N+1):
        grados=[1, 1]
        registro2=[]
        fact=1
        for i in range(1, T+1):
            
            gr=np.multiply (grados, 1/(2*i))
            j=samplea.samplea (gr)
            grados[j]=grados[j]+1
            grados.append(1)
            if i < jota:
                registro2.append(0)
            else:
                registro2.append(grados[jota]*fact)
                fact=fact*(i+1)/(i+3/2)
            
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
    plt.title('Distribucion asintotica, Pref. Attach. tree',fontsize=15)
    
    plt.show()
    