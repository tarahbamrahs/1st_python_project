#!/usr/bin/env python
# coding: utf-8

# In[17]:


l = [2.5,3,-4,5.3,6,-7]
a = 0
i = 0
while i < len(l):
    if l[i] > 0:
        a += l[i]
    i += 1
    
a

