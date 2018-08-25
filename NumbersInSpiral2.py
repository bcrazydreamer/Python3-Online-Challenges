n = int(input())
arr = [[0 for i in range(n)] for j in range(n)]
r=c=0;r1=c1=n;v=1;
for i in range(int(n/2)+1):
  #up
  for j in range(c,c1,+1):
    arr[c][j]=v
    v+=1
  r+=1

  #right
  for j in range(r,r1,+1):
    arr[j][c1-1]=v
    v+=1
  c1-=1

  #down
  for j in range(c1,c,-1):
    arr[c1][j-1]=v
    v+=1
  r1-=1

  #left
  for j in range(r1-1,r-1,-1):
    arr[j][r-1]=v
    v+=1
  c+=1
  
    
for i in arr:
  for j in i:
    print(j,end='\t')
  print()
