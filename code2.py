#!/usr/bin/env python
# coding: utf-8

# In[3]:


def if_even(num):
    even = "It is an even number"
    odd = "It is an odd number"
    if num % 2== 0:
        return even
    return odd
    
if_even(3)

