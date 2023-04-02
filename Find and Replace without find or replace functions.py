#!/usr/bin/env python
# coding: utf-8

# In[7]:


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

