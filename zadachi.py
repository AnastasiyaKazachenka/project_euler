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




#zadacha5

def prime_numbers(x):
    k = 1
    factor_list = []
    while (x >= k):        
        for n in range(2,100000) :
            if (x%n == 0) :
                factor_list.append(n)                
                k = n
                x = x/k
                break
    return (factor_list)

list1 = []
for number in range (2,21):
    list2 = prime_numbers(number)
    list3 = prime_numbers(number)
    g = []
    for x in range(0, len(list2)):
        if (list2[x] in list1) :
            g.append(list2[x])
            list1.remove(list2[x])
            list3.remove(list2[x])
    list1 = list1+list3+g

my_answer = 1
for x in range (0, len(list1)):
    my_answer = my_answer*list1[x]

print my_answer

#zadacha6

number1 = 1
for x in range (2,101):
    number1 = number1+x*x

number2 = 0
for x in range (1,101) :
    number2 = number2+x

number2 = number2*number2
number3 = number2-number1
print(number3)


