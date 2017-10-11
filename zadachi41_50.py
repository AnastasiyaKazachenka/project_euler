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
