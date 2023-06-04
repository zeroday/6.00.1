# -*- coding: utf-8 -*-
"""
Unit 1: Python Basics / Problem Set 1
Assume s is a string of lower case characters.

Write a program that counts up the number of vowels contained in the string s. 
Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. For example, 
if s = 'azcbobobegghakl', your program should print:
    Number of vowels: 5
"""

s = 'azcbobobegghakl'

def countvowels(s):
    vowels = 0
    for letter in s:
        if letter == 'a':
            vowels+=1
        elif letter == 'e':
            vowels+=1
        elif letter == 'i':
            vowels+=1
        elif letter == 'o':
            vowels+=1
        elif letter == 'u':
            vowels+=1
            
    return vowels


#print the variable s
vowel_count = "none"
vowel_count = str(countvowels(s))

print("Number of vowels: " + vowel_count)