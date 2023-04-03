#!/usr/bin/env python
# coding: utf-8

# In[ ]:


# This is the basic coding 

a = eval(input('Please enter any whole number between 0-10: '))
if a==0:
    print('This number is Zero')
elif a==1:
    print('This number is One')
elif a==2:
    print('This number is Two')
elif a==3:
    print('This number is Three')
elif a==4:
    print('This number is Four')
elif a==5:
    print('This number is Five')
elif a==6:
    print('This number is Six')
elif a==7:
    print('This number is Seven')
elif a==8:
    print('This number is Eight')
elif a==9:
    print('This number is Nine')
elif a==10:
    print('This number is Ten')
else: 
    print('The provided input is out of my scope.')


# In[1]:


# Using format string

a = eval(input('Please enter any whole number between 0-10: '))
if a==0:
    print(f'The word form of number {a} is Zero')
elif a==1:
    print(f'The word form of number {a} is One')
elif a==2:
    print(f'The word form of number {a} is Two')
elif a==3:
    print(f'The word form of number {a} is Three')
elif a==4:
    print(f'The word form of number {a} is Four')
elif a==5:
    print(f'The word form of number {a} is Five')
elif a==6:
    print(f'The word form of number {a} is Six')
elif a==7:
    print(f'The word form of number {a} is Seven')
elif a==8:
    print(f'The word form of number {a} is Eight')
elif a==9:
    print(f'The word form of number {a} is Nine')
elif a==10:
    print(f'The word form of number {a} is Ten')
else: 
    print('The provided input is out of my scope.')


# In[2]:


# Writing program for any number table in ascending order


n = int(eval(input("Which number's table would you like to see? Your answer: ")))
i = 1
while i <= 10:
    print(f'{n} x {i} = {n*i}')
    i += 1


# In[3]:


# Writing program for any number table in descending order

n = int(eval(input("Which number's table would you like to see? Your answer: ")))
i = 10
while i > 0:
    print(f'{n} x {i} = {n*i}')
    i -= 1

