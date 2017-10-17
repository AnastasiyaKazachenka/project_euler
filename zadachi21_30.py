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
