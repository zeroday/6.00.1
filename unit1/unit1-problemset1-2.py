# -*- coding: utf-8 -*-
"""
Unit 1: Python Basics / Problem Set 2
Problem 2
0.0/10.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the number of times 
the string 'bob' occurs in s. For example, 
if s = 'azcbobobegghakl', 
then your program should print

Number of times bob occurs is: 2
"""

#s = 'azcbobobegghakl'
s = 'bobbdioboblgboobobvoboboobobbuooabobobbo'

def countbobs(s):
    bobs = 0
    for x in range(0,len(s)):
        if x > (len(s)-3):
            break
        if s[x] == 'b':
            if s[x+1] == 'o':
                if s[x+2] == 'b':
                    bobs+=1

    return bobs


#print the variable s
bob_count = "none"
bob_count = str(countbobs(s))

print("Number of times bob occurs is: " + bob_count)