#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:54:02 2017

@author: Michael Su

@question: Write code to reverse a String
"""

text = list(input("Please input text : "))

length = len(text)
for i in range(0, length // 2):
    temp = text[i]
    j = length - 1 - i;
    text[i] = text[j]
    text[j] = temp
    
print(''.join(text))
