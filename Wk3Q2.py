# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 01:18:45 2020

@author: Owais Raza
"""


sentence = "students flock to the arb for a variety of outdoor activities such as jogging and picnicking"
words = sentence.split(" ")
count = 0

for i in words:
    if i[0] == i[-1]:
        count += 1

same_letter_count = count

