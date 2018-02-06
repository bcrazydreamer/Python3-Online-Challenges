n=int(input())
nam=[]
num=[]
for i in range(n):
    record=input().split()
    nam.append(record[0])
    for i in range(1,len(record)):
           record[i] = int(record[i])
    total=record[1]+record[2]+record[3]
    num.append(total)
a=min(num)
popmin=num.index(a)
print(nam[popmin])
print(round(a,2))
