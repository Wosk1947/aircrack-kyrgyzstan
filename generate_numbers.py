#!/usr/bin/env python
# coding: utf-8

import random

digits_count = 6 #amount of digits to be appended after prefixes
random_digits = 3 #amount of digits from end that will not be fully cycled through but will be chosen at random

prefixes_text = open("C:\\files\\prefixes.txt","r", encoding="utf8")
prefixes_strings_list = prefixes_text.read().split("\n")
prefixes_lists = []
for string in prefixes_strings_list:
    prefixes_list = string.split(",")
    prefixes_lists.append(prefixes_list) 
    
numbers = []    
    
def append_digits(string, count, randoms):
    if count > randoms:
        for i in range(0, 10):
            string_local = string
            string_local += str(i)
            append_digits(string_local, count-1, randoms)
    else:
        for i in range(0, randoms):
            string += str(random.randint(0, 9))
        numbers.append(string)

def append_prefixes_and_digits(string, list_number):
    if list_number < len(prefixes_lists):
        for i in range(0,len(prefixes_lists[list_number])):
            string_local = string
            string_local += prefixes_lists[list_number][i]
            append_prefixes_and_digits(string_local, list_number + 1)
    else:
        count = digits_count
        append_digits(string,count,random_digits)
        
append_prefixes_and_digits("", 0)
    
numbers_file = open("C:\\files\\numbers.txt", "w")
numbers_file.write("\n".join(numbers))

