#!/bin/python3
import sys
md=0
mind=0
def revisedRussianRoulette(doors):
   global md
   global mind
   count=0
   k=''
   arr=[]
   for i in range(len(doors)):
      if doors[i]==1:
         md=md+1;
   for j in range(len(doors)):
      if doors[j]==1:
         k=k+"1"
      else:
         k=k+" "
   arr.append(k)
   a=arr[0]
   b=a.split()
   for x in range(len(b)):
    c=len(b[x])
    div=c/2+0.5
    div=int(div)
    count=count+div
   mind=count   
   ans=str(mind)+" "+str(md)
   return ans
if __name__ == "__main__":
    n = int(input().strip())
    doors = list(map(int, input().strip().split(' ')))
    result = revisedRussianRoulette(doors)
    print(result)
