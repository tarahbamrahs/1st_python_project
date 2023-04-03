#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Basic code

text = input('What text would you like to use for this project? ')
n = int(eval(input(f'How many characters would you like to remove of the word - {text}? ')))
d = input(f'From which side would you like to remove {n} characters of the word - {text} [put "R" for Right or "L" for Left]: ').upper
if d == 'L':
    print(text[n: ])
else:
    print(text[ :(len(text)-n)])


# In[4]:


# Additional scenarios

text = input('What text would you like to use for this project? ')
n = int(eval(input(f'How many characters would you like to remove from the word - "{text}"? ')))
d = input(f'From which side would you like to remove {n} characters of the "{text}" [enter "R" for Right or "L" for Left]: ').upper
if d == 'L':
    print(text[n: ])
else:
    print(text[ :(len(text)-n)])
    
happy = input('Are you happy with the output [enter "Y" for Yes or "N" for No]: ')
if happy == 'Y':
    print('I am glad. See you soon!')
else:
    more = input(f'What else would you like to do with the word "{text}"?\n[enter "R" if you want to reverse the order of this word\nenter "P" if you want a part of this word]: ')
 
if more == 'R':
    print(text[(len(text)-1): :-1])
else:
    begin = int(eval(input(f'What is the starting index number of this part? [enter any number between 0 to {len(text)}]: ')))
end = int(eval(input(f'What is the ending index number of this part? [enter any number {begin+1} to {len(text)}]: ')))
if begin < end:
    print(text[begin:end])
else:
    end = int(eval(input(f'Please note: the ending number {end} is an invalid choice. Kindly enter a number which is between {begin+1} to {len(text)} only: ')))
if begin < end:
    print(text[begin:end])
else:
    print('Sorry there seems to be an issue with the input.')

