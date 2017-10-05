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
def reversed_string(a_string):
    return a_string[::-1]
n1 = 100001
n2 = 999999
total_umnosit = []
for i in range(n1,n2,11):
    x = i
    k = 1
    a = 0
    factor_list = []
    while (x > 99) and (a != k):    
        a = 1
        for n in range(999,1,-1) :
            if (x%n == 0) :
                factor_list.append(n)
                a = n
                k = a
                x = x/k
                break
        check = i/a
        if (check>99 and check<1000):
            total_umnosit.append(i)

my_len = len(total_umnosit)
polyndroms = []
for x in range (0, my_len):
    a = str(total_umnosit[x])
    b = reversed_string(a)
    if (a==b) :
        polyndroms.append(total_umnosit[x])
max(polyndroms)

