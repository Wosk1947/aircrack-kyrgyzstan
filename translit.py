#!/usr/bin/env python
# coding: utf-8

strings_russian_text = open("C:\\files\\names_russian.txt","r", encoding="utf8")
strings_russian_list = strings_russian_text.read().split("\n")
characters_map_text = open("C:\\files\\translit_map.txt","r", encoding="utf8")
characters_map_as_list = characters_map_text.read().split("\n")

original_strings_lists = []
substitution_strings_lists = []
for entry in characters_map_as_list:
    original_and_substitution_lists = entry.split("=")
    original_list = original_and_substitution_lists[0].split("|")
    substitution_list = original_and_substitution_lists[1].split("|")
    original_strings_lists.append(original_list)
    substitution_strings_lists.append(substitution_list)
    
strings_latin_list = []
for string_russian in strings_russian_list:
    latin_strings_for_current_string = [""]
    index = 0
    for char in string_russian:
        i = 0
        for entry in original_strings_lists:
            for original_char in entry:
                if original_char == char:
                    index = i
            i = i + 1        
        substitution_strings = substitution_strings_lists[index]
        if len(substitution_strings) != 0:
            latin_strings_for_current_string_original = latin_strings_for_current_string.copy()
            latin_strings_for_current_string = []
            for i in range(0, len(substitution_strings)):
                tmp_list = latin_strings_for_current_string_original.copy()
                for j in range(0,len(tmp_list)):
                    tmp_list[j] += substitution_strings[i]
                latin_strings_for_current_string.extend(tmp_list)    
    strings_latin_list.extend(latin_strings_for_current_string)
    
strings_latin_file = open("C:\\files\\names_latin.txt", "w")
strings_latin_file.write("\n".join(strings_latin_list))


