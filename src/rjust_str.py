#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 10, 2014

@author: anroco

In python how to right justify a string?

En python ¿como justificar a la derecha un string?
'''

#create a str
s = 'many years later'
print(s)

#generates a string of length defined, where is right justified the string 's'.
s_right = s.rjust(30)
print(s_right)

#can specify the padding character
s_right = s.rjust(30, '-')
print(s_right)
