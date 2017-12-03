#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Dec  3 20:27:13 2017

@author: Michael Su

@question:
Implement an algorithm to determine if a string has all unique characters
What if you can not use additional data structures?
"""

text = list(input("Please input text : "))
text.sort()
for i in range(0, len(text) - 1):
    if text[i] == text[i + 1]:
        print("found duplicated char '{}'".format(text[i]))
        break
else:
    print("no duplicated char is found")