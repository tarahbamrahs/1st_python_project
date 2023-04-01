#!/usr/bin/env python
# coding: utf-8

# In[86]:


t = 'Jupyter'
print(f'The given word for the day is "{t}".')
find_value = input('Enter the finding value: ').lower()
new_value = input('Enter the replacing value: ').lower()
i = 0
while i < len(t):
    if t[i] == find_value:
        a = t[:i]
        b = t[i+1:]
    i += 1
print(a + f'{new_value}'+ b)


# In[ ]:


t = 'text'
r = '7'
print(t[:1]+f'{r}'+t[2:])


# In[40]:


t = 'text'
r = 'x'
t.index(r)


# In[66]:


t = 'text'
r = 'x'
i = 0
while i < len(t):
    if t[i] == r:
        a = t[:i]
        b = t[i+1:]
    i += 1
print(a)
print(b)


# In[63]:


t = 'text'
print(t[2:])

