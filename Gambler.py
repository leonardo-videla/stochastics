#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Aug 27 18:59:33 2022

@author: leonardovidela
"""

import random as rd
from  matplotlib import pyplot as plt

def Gambler (M, p, i):
    cur=i
    k=0
    while cur*(M-cur) != 0:
        k=k+1
        if rd.random ()< p:
            cur=cur+1
        else:
            cur=cur-1  
     
    return [k, cur]


def Gambler_stat (M, prob, nsamples):
    props=[1]
    times=[0]
    for i in range (M-1):
        p=0
        t=0
        for _ in range(nsamples):
           [k,cur]=Gambler (M, prob, i+1)
           t=t+k
           if cur==0:
               p=p+1
        times.append(t/nsamples)
        props.append(p/nsamples)
    props.append(0)
    times.append(0)

    plt.plot (times)
    plt.show()
    plt.plot (props)
    plt.show()