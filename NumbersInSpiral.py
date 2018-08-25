n =int(input())
arr=[]
for i in range(n):
    arr.append([int(0) for i in range(n)])
r=c=0;r1=c1=n
val=1
for i in range(int(n/2)):
  #up
  for j in range(c,c1):
    arr[r][j]=val
    val=val+1
  c1=c1-1
  r=r+1

  #right
  for j in range(r,r1):
    arr[j][c1]=val
    val=val+1
  r1=r1-1
  c=c+1

  #down
  for j in range(c,c1+1):
    arr[r1][c1+i-j]=val
    val=val+1

  #left
  for j in range(r,r1):
    arr[c1+i-j][c-1]=val
    val=val+1
    
if(n%2!=0):
  arr[int(n/2)][int(n/2)]=val
  
for i in arr:
  for j in i:
    spiral=''
    if(j<10):
      space='    '
    elif(j>99):
      space='  '
    else:
      space='   '
    print(j,end=space)
  print()

