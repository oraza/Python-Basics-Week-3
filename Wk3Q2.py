# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:18:45 2020

@author: Owais Raza
"""
#The variable sentence stores a string. Write code to determine how many words 
#in sentence start and end with the same letter, including one-letter words. 
#Store the result in the variable same_letter_count.
#Hard-coded answers will receive no credit.

sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
words = sentence.split(" ")
count = 0

for i in words:
    if i[0] == i[-1]:
        count += 1

same_letter_count = count

