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
