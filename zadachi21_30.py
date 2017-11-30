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

<<<<<<< HEAD
#zadacha23
import math
def find_devisors(some_number) :
    devisors = [1]
    a = int(round(math.sqrt(some_number)))
    for x in range(2,a+1):
        if some_number%x == 0 :
            devisors.append(x)
            if some_number/x != x :
                devisors.append(some_number/x)
    return (devisors)
    
def find_sum_of_devisors(x) :
    sum_of_devisors = 0
    list_of_devisors = find_devisors(x)
    for z in range (0, len(list_of_devisors)) :
        sum_of_devisors = sum_of_devisors+list_of_devisors[z]
    return (sum_of_devisors)
    
list_of_abundant = []
for x in range(11,28123) :
    if find_sum_of_devisors(x) > x :
        list_of_abundant.append(x)


list_of_ab_sum = []
x=0
while x < len(list_of_abundant):
    for k in range(x, len(list_of_abundant)) :
        n = list_of_abundant[x]+list_of_abundant[k]
        if n < 28124:
            list_of_ab_sum.append(n)
    x = x+1
    
list_of_ab_sum = set(list_of_ab_sum)


list_of_not_ab_sum = []
for x in range(1,28124):
    if x not in list_of_ab_sum :
        list_of_not_ab_sum.append(x)
    
final_sum = 0
for z in range (0, len(list_of_not_ab_sum)) :
    final_sum = final_sum+list_of_not_ab_sum[z]


=======
    
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
>>>>>>> e15cb3eb7978068758256ead6e2d1e06379ff4ab
