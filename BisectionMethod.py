#!/usr/bin/env python
# coding: utf-8

# In[3]:


import numpy as np
import pandas as pd
import math
import matplotlib.pyplot as plt


# In[4]:


def f(x):
    
        return (x-1)**3 + 0.510


# In[5]:


def Bisection(a,b):
    i=0
    while(np.abs(a-b))>0.0001:
        mid = (a+b)/2
        
        if(f(a)*f(mid))<0.0001:
            b=mid
        else:
            a=mid
        i+=1
        print('a :',a ,'b  :',b,' mid :',mid)
    return mid


# In[8]:


root=Bisection(2,0)


# In[7]:


f(2)*f(0)


# In[6]:


f(0.19635009765625)


# In[ ]:




