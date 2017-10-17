#zadacha48

sum = 0
for n in range(1,1001):
    l=1
    k=1
    while k<n+1:
        l = l*n
        k = k+1
    sum = sum+l
number = str(sum)
number[-10:]



#zadacha50

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
                        

k = 0
x = 1
counter = []
primek = []
while k+x < 1000000 :
    x = x+1
    if isPrime(x):
        k = k+x
        counter.append(x)


for x in range(0, len(counter)):
        k = k-counter[x]
        if isPrime(k):
            primek.append(k)
