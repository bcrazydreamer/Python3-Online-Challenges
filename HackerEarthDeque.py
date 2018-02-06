from collections import deque
dq = deque()
i=1
n=int(input())
while(i<=n):
    s =input().split()
    if s[0] == 'append':
        dq.append(s[1])
    elif s[0] == 'appendleft':
        dq.appendleft(s[1])
    elif s[0] == 'appendright':
        dq.appendright(s[1])
    elif s[0] == 'pop':
        dq.pop()
    elif s[0] == 'popright':
        dq.popright()
    else:
        dq.popleft()
    i=i+1
print(" ".join(dq))
