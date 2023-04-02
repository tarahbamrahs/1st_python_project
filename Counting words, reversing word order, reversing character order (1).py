#!/usr/bin/env python
# coding: utf-8

# In[3]:


# This cell is for "Counting Words" code



text = input('Enter the statement here: ')
a = text.split()
list
print(f'There are total of {len(a)} words in this statement')


# In[4]:


# This cell is for reversing the order of words in the statement using initial index as 0


text = input('Enter the statement here: ')
list = text.split()
list
i = 0
while i < len(list):
    print(list[-(i+1)], end = ' ')
    i += 1


# In[18]:


# This cell is for reversing the order of words in the statement using initial index as last index value


text = input('Enter the statement here: ')
list = text.split()
i = len(list)-1
while i >= 0:
    print(list[i], end = ' ')
    i -= 1


# In[106]:


# This cell is for reversing the order of characters in the statement



text = input('Enter the statement here: ')
i = 0
while i < len(text):
    print(text[-(i+1)], end = '')
    i += 1

