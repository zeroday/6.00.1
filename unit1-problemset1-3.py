# -*- coding: utf-8 -*-
"""
Unit 1: Python Basics / Problem Set 3
Problem 3

Problem 3
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
s = 'abcbcd'
#s = 'azcbobobegghakl'


def countalphabetical(s): 
    current_word = []
    string_array = []
    longest_string = []

    for letter in list(s):
        string_array.append(letter)

    """
     track the longest word with one variable
     track the current word with another variable
     reset the current word when the ordinal value of the next 
     character in the string is higher

    """    
    # reset the word on what condition?
    # set longest_string = current_word under what condition?
    for i in range(0,len(s)):
        if (i > (len(s)-2)):
            continue
        if (ord(string_array[i]) <= ord(string_array[i+1])):
            current_word.append(string_array[i])
        if (ord(string_array[i]) == ord(string_array[i+1])):
            current_word.append(string_array[i])

        print(len(current_word),len(longest_string))
        print(current_word)
        print(longest_string)
        if len(current_word) > len(longest_string):
            longest_string = current_word
            current_word = []

    return longest_string


#print the variable s
longest_string = "none"
longest_string = str(countalphabetical(s))

print("Longest substring in alphabetical order is: " + longest_string)