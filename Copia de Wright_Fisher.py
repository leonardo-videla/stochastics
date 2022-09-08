#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 15:42:28 2022

@author: leonardovidela
"""

import numpy as np
from  matplotlib import pyplot as plt

def Wright_Fisher (M,  i, nmax=-1):
    wf=[i]
    cur=i
    k=0
    finished=False
    while not finished:
        k=k+1
        cur=np.random.binomial (M, cur/M)
        wf.append(cur)
        if (cur * (M-cur)==0) or (nmax > 0 and k > nmax):
            finished=True
     
    return wf, k, cur

def W_F_stat (M, nsamples):
    props=[1]
    for i in range (M-1):
        p=0
        for j in range(nsamples):
           _, _, final=Wright_Fisher (M, i+1)
           if final==0:
               p=p+1
        props.append (p/nsamples)
    props.append(0)
    plt.plot (props)
    
    



