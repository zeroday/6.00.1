# -*- coding: utf-8 -*-
"""
Unit 1: Python Basics / Problem Set 3

0.0/15.0 points (graded)
Assume s is a string of lower case characters.

Write a program that prints the longest substring of s 
in which the letters occur in alphabetical order. 
For example, if s = 'azcbobobegghakl', 
then your program should print

Longest substring in alphabetical order is: beggh
In the case of ties, print the first substring. 
For example, if s = 'abcbcd', then your program should print

Longest substring in alphabetical order is: abc
Note: This problem may be challenging. 
We encourage you to work smart. 
If you've spent more than a few hours on this problem, 
we suggest that you move on to a different part of the course. 
If you have time, come back to this problem after you've had a 
break and cleared your head.
"""

s = 'azcbobobegghakl'
#s = 'abcdefghijklmnopqrstuvwxyz'

def biggest_list(word_list):
    # list of keys sorted by size
    # return the top of the list
    biggest_word = ''
    for i in range(0,len(word_list)):
        if len(word_list[i]) > len(biggest_word):
            biggest_word = word_list[i]

    return biggest_word


def countalphabetical(s):
    current_word = []
    longest_alphabetical = []
    word_list = []
    string_as_list = list(s)
    
    for pos in range(0,(len(s))):
        current_position = ord(string_as_list[pos])
        if (pos == (len(s)-1)):
            next_position = 0
        else:
            next_position = ord(string_as_list[pos+1])
        current_word.append(string_as_list[pos])
        if current_position > next_position:
            word_list.append(current_word)
            current_word=[]
                
    longest_alphabetical = biggest_list(word_list)
        

    return longest_alphabetical


#print the variable s
longest_string = "none"
longest_string = countalphabetical(s)
printable_string = ''

for character in longest_string:
    printable_string = printable_string + character

    
print("Longest substring in alphabetical order is: " + printable_string)
