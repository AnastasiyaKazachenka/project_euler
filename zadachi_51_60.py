
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

#zadacha54
high_card = (["2"],["3"],["4"],["5"],["6"],["7"],["8"],["9"],["T"],["J"],["Q"],["K"],["A"])
one_pair = (["2","2"],["3","3"],["4","4"],["5","5"],["6","6"],["7","7"],["8","8"],["9","9"],["T","T"],["J","J"],["Q","Q"],["K","K"],["A","A"])
two_pairs = []
for x in range(0,len(one_pair)) :
    for y in range(x,len(one_pair)) :
        if x != y :
            two_pairs.append(one_pair[x]+one_pair[y])

two_pairs=[sorted(x) for x in two_pairs]
           
three_cards = (["2","2","2"],["3","3","3"],["4","4","4"],["5","5","5"],["6","6","6"],["7","7","7"],["8","8","8"],["9","9","9"],["T","T","T"],["J","J","J"],["Q","Q","Q"],["K","K","K"],["A","A","A"])
straight_cards=(["2","3","4","5","6"],["3","4","5","6","7"],["4","5","6","7","8"],["5","6","7","8","9"],["6","7","8","9","T"],["7","8","9","T","J"],["8","9","T","J","Q"],["9","T","J","Q","K"],["T","J","Q","K","A"])
straight_cards=[sorted(x) for x in straight_cards]

flush = (["H","H","H","H","H"],["C","C","C","C","C"],["S","S","S","S","S"],["D","D","D","D","D"])
full_house=[]
for x in range(0,len(one_pair)) :
    for y in range(0,len(one_pair)) :
        if x != y :
            full_house.append(one_pair[x]+three_cards[y])

full_house=[sorted(x) for x in full_house]
            
four_cards = (["2","2","2","2"],["3","3","3","3"],["4","4","4","4"],["5","5","5","5"],["6","6","6","6"],["7","7","7","7"],["8","8","8","8"],["9","9","9","9"],["T","T","T","T"],["J","J","J","J"],["Q","Q","Q","Q"],["K","K","K","K"],["A","A","A","A"])

poker_hands = [high_card,one_pair,two_pairs,three_cards,straight_cards,full_house,four_cards]



def find_hands(zz,cc) :
    zz=sorted(zz)
    cc_copy=cc[:]
    counter=0
    for x in range(0,len(zz)):
        if zz[x] in cc_copy:
            counter=counter+1
            cc_copy.remove(zz[x])
    if counter==len(cc) :
        return(True)
    else:
        return(False)

def find_combinations(list1) :
    list_to_give=[]
    for x in range(len(poker_hands)-1,-1,-1) :
        for y in range(len(poker_hands[x])-1,-1,-1) :
            if find_hands(list1,poker_hands[x][y])==True:
                list_to_give.append(poker_hands[x][y])
    return(list_to_give)


def find_highest_combinations(list1) :
    for x in range(len(poker_hands)-1,-1,-1) :
        for y in range(len(poker_hands[x])-1,-1,-1) :
            if find_hands(list1,poker_hands[x][y])==True:
                return([poker_hands[x][y],poker_hands.index(poker_hands[x]),poker_hands[x].index(poker_hands[x][y])])
                break

match_to_pokerhands = {0:"high_card",1:"one_pair",2:"two_pairs",3:"three_cards",4:"straight_cards",5:"full_house",6:"four_cards"}
pokerhands_points = {"high_card":1,"one_pair":2,"two_pairs":3,"three_cards":4,"straight_cards":5,"flush":5,"full_house":7,"four_cards":8,"straight_flush":4,"royal_flush":1}

def player_points(list1):
    p1=list1
    if p1[1] in flush :
        a=find_combinations(p1[0])
        p1_points=[]
        for x in range(0,len(a)) :
            zz=find_highest_combinations(a[x])
            if zz[1] != 0 and zz[1] != 4:
                l=pokerhands_points[match_to_pokerhands[zz[1]]]
            if zz[1] == 0 :
                l=pokerhands_points[match_to_pokerhands[zz[1]]]+5
            if zz[1] == 4 and zz[2] == 8 :
                l=pokerhands_points[match_to_pokerhands[zz[1]]]+5
            if zz[1] == 4 and zz[2] != 8 :
                l=pokerhands_points[match_to_pokerhands[zz[1]]]+4
            p1_points.append([l,zz[2]])
    else :
        a=find_combinations(p1[0])
        p1_points=[]
        for x in range(0,len(a)) :
            zz=find_highest_combinations(a[x])
            l=pokerhands_points[match_to_pokerhands[zz[1]]]
            p1_points.append([l,zz[2]])
    return(p1_points)

import urllib
txt = urllib.request.urlopen("https://projecteuler.net/project/resources/p054_poker.txt").read()
txt = txt.decode("utf-8")
txt=txt.split("\n")
txt_2=[x.split(" ") for x in txt]


player1=[]
for x in range(0,len(txt_2)-1) :
    value=[]
    suit=[]
    for y in range(0,int(len(txt_2[x])/2)):
        value.append(txt_2[x][y][0])
        suit.append(txt_2[x][y][1])
    player1.append([value,suit])

player2=[]
for x in range(0,len(txt_2)-1) :
    value=[]
    suit=[]
    for y in range(5,10):
        value.append(txt_2[x][y][0])
        suit.append(txt_2[x][y][1])
    player2.append([value,suit])       
        
player1_win=0
player2_win=0

for x in range(0,1000) :
    player1_points=player_points(player1[x])
    player2_points=player_points(player2[x])
    p1=player1_points[0]
    p2=player2_points[0]
    x=1
    while p1==p2 :
        p1=player1_points[x]
        p2=player2_points[x]
        x=x+1
    if p1[0]>p2[0] :
        player1_win=player1_win+1
    elif p1[0]== p2[0] :
        if p1[1] > p2[1] :
            player1_win=player1_win+1
        else :
            player2_win=player2_win+1
    else:
        player2_win=player2_win+1
            
            
            
            
#zadacha55

def reversed_string(a_string):
    return a_string[::-1]

def isPolyndrome (my_numb):
    a = str(my_numb)
    b = reversed_string(a)
    if (a==b) :
        return(True)
    else:
        return(False)

counter=0
my_numb=1
while my_numb<10001:
    n=0
    z=my_numb
    while n<51:
        my_numb_pol = int(reversed_string(str(z)))
        if isPolyndrome(z+my_numb_pol)==True:
            counter = counter+1
            n=52
        else:
            z=z+my_numb_pol
            n=n+1
    my_numb=my_numb+1
    
10000-counter


#zadacha56
n=1
for a in range(1,100) :
    for b in range(1,100) :
        c=sum([int(d) for d in str(a**b)])
        if c>n :
            n=c

#zadacha57

n=3
d=2
z=1
counter =[]

while z<1000:
    n=n+d
    n1=n
    n=d
    d=n1
    n=n+d
    if len(str(n))>len(str(d)):
        counter.append([n,d])
    z=z+1            

    
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


a=1
x=2
z=62
r_primes_total=0
my_total=1

while z>10:
    my_list=[]
    my_list.append(a+x)
    my_list.append(a+2*x)
    my_list.append(a+3*x)
    my_list.append(a+4*x)
    r_primes=0
    for numb in my_list :
        if isPrime(numb) :
            r_primes=r_primes+1   
    r_primes_total = r_primes_total+r_primes
    my_total=my_total+len(my_list)
    z=100*(r_primes_total)/(my_total)
    a=a+4*x
    x=x+2

print(x-1)  
