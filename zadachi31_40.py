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
