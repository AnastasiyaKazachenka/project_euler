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

#zadacha7

def prime_numbers(x):
    k = 1
    factor_list = []
    while (x >= k) and (len(factor_list)<2):        
        for n in range(2,2000000) :
            if (x%n == 0) :
                factor_list.append(n)                
                k = n
                x = x/k
                break
    return (factor_list)

list_of_primes = [2]
x = 3


while len(list_of_primes) <10001:
    k = prime_numbers(x)
    if len(k) == 1:
        list_of_primes.append(x)
    x = x+2

list_of_primes[10001]


#zadacha10
import math
def isPrime(x):
    if (x == 1) :
        return False
    else:
        if x <4 :
            return True
        else:
            if x%2 == 0:
                return False
            else:
                if x<9 :
                    return True
                else:
                    if x%3 == 0:
                        return False
                    else:
                        r = round(math.sqrt(x))
                        f = 5
                        while f<=r:
                            if x%f == 0 :
                                return False
                            if x%(f+2) == 0 :
                                return False
                            f = f+6
                        else:
                            return True

sum_of_primes = 2
x = 3
while x<2000000 :
    if isPrime(x) == True :
        sum_of_primes = sum_of_primes + x
    x = x+2



#zadacha8

my_string ="7316717653133062491922511967442657474235534919493496983520312774506326239578318016984801869478851843858615607891129494954595017379583319528532088055111254069874715852386305071569329096329522744304355766896648950445244523161731856403098711121722383113622298934233803081353362766142828064444866452387493035890729629049156044077239071381051585930796086670172427121883998797908792274921901699720888093776657273330010533678812202354218097512545405947522435258490771167055601360483958644670632441572215539753697817977846174064955149290862569321978468622482839722413756570560574902614079729686524145351004748216637048440319989000889524345065854122758866688116427171479924442928230863465674813919123162824586178664583591245665294765456828489128831426076900422421902267105562632111110937054421750694165896040807198403850962455444362981230987879927244284909188845801561660979191338754992005240636899125607176060588611646710940507754100225698315520005593572972571636269561882670428252483600823257530420752963450"

the_bigest_prduct = 0

def find_product(some_string):
    if "0" in some_string :
        return 0
    else:
        k = 1
        for x in range(0,len(some_string)):
            a = int(some_string[x])
            k = k*a
        return k

for x in range(0,986):
    some_string = my_string[x:(x+13)]
    some_product = find_product(some_string)
    if some_product > the_bigest_prduct:
        the_bigest_prduct = some_product

print the_bigest_prduct
