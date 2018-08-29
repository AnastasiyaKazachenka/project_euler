#zadacha 31

import time
start = time.time()

counter=0
   for a in range(0,201) :
       for b in range(0,101):
           for c in range(0,41):
               for d in range(0,21) :
                   for e in range(0,11) :
                       for f in range(0,5) :
                           for j in range(0,3) :
                               for h in range(0,2) :
                                  if a*1+b*2+c*5+d*10+e*20+f*50+j*100+h*200==200 :
                                      counter = counter+1

end = time.time()
print(end - start)

a=[1]*201
coin=[2,5,10,20,50,100,200]
for c in coin:
    for i in range(c,201):
        a[i]+=a[i-c]

      
      
#zadacha32
        
import itertools

counter=[]

a=list(itertools.permutations(range(1,10)))

for x in range(0,len(a)-1):
    if a[x][0]*(a[x][1]*1000+a[x][2]*100+a[x][3]*10+a[x][4])==a[x][5]*1000+a[x][6]*100+a[x][7]*10+a[x][8] :
        counter.append(a[x][5]*1000+a[x][6]*100+a[x][7]*10+a[x][8])
    if (a[x][0]*10+a[x][1])*(a[x][2]*100+a[x][3]*10+a[x][4])==a[x][5]*1000+a[x][6]*100+a[x][7]*10+a[x][8] :
        counter.append(a[x][5]*1000+a[x][6]*100+a[x][7]*10+a[x][8])

counter=set(counter)
sum(counter)

#zadacha 33

a=list(range(10,98))
up=[]
down=[]

for x in a :
    if x%10 != 0 :
        first_n = x//10
        second_n = x%10
        for z in range(1,10) :
            if (x/(z*10+first_n)==second_n/z and second_n/z<1) :
                up.append(x)            
                down.append(z*10+first_n)
            if (x/(second_n*10+z)==first_n/z and first_n/z<1) :
                up.append(x)            
                down.append(second_n*10+z)


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

up_pr=1
for x in up:
    up_pr = up_pr*x
    
down_pr=1
for x in down:
    down_pr = down_pr*x

up_mnoz = prime_numbers(up_pr)
down_mnoz = prime_numbers(down_pr)

for x in range(0,len(up_mnoz)) :
    if up_mnoz[x] in down_mnoz :
        down_mnoz.remove(up_mnoz[x])

answer=1
for x in down_mnoz:
    answer = answer*x

      
#zadacha34
import math
import itertools

a=list(range(0,10))
b = [math.factorial(x) for x in a]
for x in range(0,len(a)):
    a[x]=str(a[x])


dd = dict(zip(a,b))


x=1
y=362880

while x<len(str(y)) :
    x= x+1
    y=y+362880

my_lists = []
for numb in range(11,y+1):
    numb_break = list(str(numb))
    my_sum = 0
    for ff in numb_break:
        my_sum=my_sum+dd[ff]
    if my_sum==numb :
        my_lists.append(numb)

sum(my_lists) 


#zadacha35
import math
import itertools
from collections import deque
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

my_primes=[]  
for x in range(1,1000000) :
    if isPrime(x)==True :
        k=[int(y) for y in str(x)]
        a=deque(k)
        zz=[]
        for x in range(len(a)):
            a.rotate(1)
            zz.append(list(a))
        counter=0
        for n in range(0,len(zz)) :
            number = int("".join([str(y) for y in zz[n]]))
            if isPrime(number)==False :
                counter=1
        if counter==0:
            my_primes.append(x)

            
#zadacha36

def dec_to_bin(x):
    return int(bin(x)[2:])

def reversed_string(a_string):
    return a_string[::-1]

polyndroms = []
for x in range(1,1000000):
    x2=x
    a = str(x2)
    b = reversed_string(a)
    if (a==b) :
        g=dec_to_bin(x)
        g=str(g)
        h=reversed_string(g)
        if g==h :
            polyndroms.append(x)

sum(polyndroms)
