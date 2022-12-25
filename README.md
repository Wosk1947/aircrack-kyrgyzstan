# aircrack-kyrgyzstan
Useful info and Python scripts for cracking WI-FI passwords in Kyrgyzstan

## Introduction

This repository contains some info and python scripts for generating passwords or parts of passwords to be used with aircrack-ng to crack WI-FI networks in Kyrgyzstan. Because Kyrgyzstan is a far east country, most of widespread wordlists with probable wi-fi passwords won't work very well on its territory. Moreover Kyrgyzstan is a former Soviet Union republic with heavy influence of russian culture and language, and russian language is still widely used in there, mobile phones and computers too, so passwords will likely be cyrillic-based. Also many internet providers on CIS territories use mobile phones as default password for a new client. This repo contains a list of Kyrgyzstan names in russian (*names_russian.txt*), a *translit.py* script that phonetically transliterates russian symbols to latin and *generate_numbers.py* script that generates kyrgyzstan mobile phone numbers.  

1. **translit.py** uses two files - list of russian words and a map where each russian symbol has its phonetic equivalent (or several) in latin symbols. This map is in file *translit_map*. The resulting file is *names_latin.txt*. Also there is another map - *projected_keyboard_map.txt*. This map covers the situation when a user types their's name with russian symbols, but the keyboard layout is latin. The resulting file is *names_projected.txt*.

2. **generate_numbers.py** generates kyrgyzstan mobile phone numbers. It uses a file *prefixes.txt* that contains list of prefixes. Each line of this file contains a list of possible prefixes for this position, so each number is some prefix from line 1 + some prefix from line 2 + ... + some amount of 0-9 digits. Line 1 contains prefixes 0, 996(a world prefix for Kyrgyzstan) and just an empty space. Line 2 contains differen mobile providers prefixes:

220,221,222,223,224,225,226,227,228,770,771,772,773,774,775,776,777,778,779 - Beeline Kyrgyzstan
559,558,557,556,555,554,553,552,551,550,755,990,995,997,998,999 - MegaCom Kyrgyzstan
500,501,502,503,504,505,506,507,508,509,700,701,702,703,704,705,706,707,708,709 - O! Kyrgyzstan

After prefixes 6 digits 0-9 must be added to complete the number. You can modify script to add any amount of digits. Also there is a *random_digits* parameter. It is needed to make the resulting file and computation time smaller. It corresponds to amount of digits from end of number that won't be fully cycled through but rather chosen at random.
