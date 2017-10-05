# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

#zadacha 1

sum = 0
for x in range(1,1001):
    if (x%3 == 0) or (x%5 == 0):
        sum = sum+x
     
     
#zadacha3
import math
         
x = 989989
k = 1
factor_list = []
while (x > k):    
    a = 1
    for n in range(2,100000) :
        if (x%n == 0) :
            factor_list.append(n)
            a = n
            k = a
            x = x/k
            break
        
        
#zadacha4


        
