from collections import OrderedDict
n=int(input())
i=1
j=1
cunt=''
arry=OrderedDict()
count=1
while(i<=n):
    abc=input()
    if abc not in arry:
        arry[abc]=count
        
    else:
        arry[abc]+=count
    i=i+1
for item,netcount in arry.items():
    j=j+1
print(j-1)
for item,netcount in arry.items():
    cunt=cunt+str(netcount)+' '
print(cunt)    

    
