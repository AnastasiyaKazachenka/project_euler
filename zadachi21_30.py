#zadacha21
import math

def dev_sum(x):
    devisors_sum=1
    for k in range(2,int(math.sqrt(x))):
            if x%k == 0 :
                devisors_sum = devisors_sum+k+x/k
    return(devisors_sum)

final_sum=0
for x in range(2,10000):
    sum_x_dev = dev_sum(x)
    to_compare = dev_sum(sum_x_dev)
    if x == to_compare and sum_x_dev != to_compare :
        final_sum = final_sum+x


#zadacha22

from string import ascii_uppercase as al

dic = {x:i for i, x in enumerate(al, 1)}

with open('names.txt') as fp:
    names = fp.read().split('","')
names[0] = "MARY"
names[-1] = "ALONSO"
names = sorted(names)

biggest = 0
for x in range(0, len(names)) :
    k = 0
    for y in range(0,len(names[x])):
        k = k+dic[names[x][y]] 
    final_number = k*(x+1)
    biggest = biggest+final_number

    
#zadacha25
            
x =1
y =1
counter = 2
length_k = len(str(x))

while length_k < 1000:
    z = x+y
    counter = counter+1
    length_k = len(str(z))
    x = y
    y = z    
