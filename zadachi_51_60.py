
#zadacha51

from sympy import prime
from sympy import primepi
from sympy.ntheory import isprime

n=primepi(56993)+1

def first_check(my_prime):
    my_prime=str(my_prime)
    answer=[]
    if (my_prime.count("0")>1) :
        answer.append(0)
    if (my_prime.count("1")>1):
        answer.append(1)
    if (my_prime.count("2")>1) :
        answer.append(2)
    return(answer)

def count_primes(my_pattern,z):
    numbs=[str(k) for k in range(z,10)]
    list_of_primes=[]
    for x in range(0,len(numbs)) :
        list_of_primes.append(int(my_pattern.replace("x",numbs[x])))
    counter=0
    for n in range(0,len(list_of_primes)) :
        if isprime(list_of_primes[n])==True :
            counter=counter+1
    return(counter)

    

while True:
    if len(first_check(prime(n))) ==1:
        my_prime_pattern=str(prime(n))
        my_prime_pattern=my_prime_pattern.replace(str(first_check(prime(n))[0]),"x")
        if count_primes(my_prime_pattern,first_check(prime(n))[0]) == 8:
            print(prime(n))
            break
    if len(first_check(prime(n))) ==2:
        my_prime_pattern_a=str(prime(n))
        my_prime_pattern_a=my_prime_pattern_a.replace(str(first_check(prime(n))[0]),"x")
        my_prime_pattern_b=str(prime(n))
        my_prime_pattern_b=my_prime_pattern_b.replace(str(first_check(prime(n))[1]),"x")
        if count_primes(my_prime_pattern_a,first_check(prime(n))[0]) == 8 or count_primes(my_prime_pattern_b,first_check(prime(n))[1]) == 8:
            print(prime(n))
            break
    if len(first_check(prime(n))) ==3:
        my_prime_pattern_a=str(prime(n))
        my_prime_pattern_a=my_prime_pattern_a.replace(str(first_check(prime(n))[0]),"x")
        my_prime_pattern_b=str(prime(n))
        my_prime_pattern_b=my_prime_pattern_b.replace(str(first_check(prime(n))[1]),"x")
        my_prime_pattern_c=str(prime(n))
        my_prime_pattern_c=my_prime_pattern_b.replace(str(first_check(prime(n))[2]),"x")
        if count_primes(my_prime_pattern_a,first_check(prime(n))[0]) == 8 or count_primes(my_prime_pattern_b,first_check(prime(n))[1]) == 8 or count_primes(my_prime_pattern_c,first_check(prime(n))[2]) == 8:
            print(prime(n))
            break
    n=n+1
    
    
    #zadacha52

n=100000
while True:
    x1=n
    a=sorted([int(d) for d in str(x1)])
    x2=sorted([int(d) for d in str(2*x1)])
    x3=sorted([int(d) for d in str(3*x1)])
    x4=sorted([int(d) for d in str(4*x1)])
    x5=sorted([int(d) for d in str(5*x1)])
    x6=sorted([int(d) for d in str(6*x1)])
    if a==x2 and a==x3 and a==x4 and a==x5 and a==x6:
        print(n)
        break
    n=n+1

# zadacha53
import math
math.factorial(7)

counter=0

for n in range(1,101):
    for r in range(1,n+1):
        if math.factorial(n)/(math.factorial(r)*math.factorial(n-r)) >1000000 :
            counter=counter+1
