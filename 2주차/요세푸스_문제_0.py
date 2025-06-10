import sys
from collections import deque
input=sys.stdin.readline
N,K=map(int,input().split()) 
queue=deque()
result=[]
for i in range(1,N+1):
    queue.append(i)

while queue:
    for _ in range(K-1):
        queue.append(queue.popleft())
    result.append(queue[0])
    queue.popleft()   


print("<",end='')
for i in range(len(result)-1):
    print(result[i],end=', ')
print(f'{result[-1]}',end='')
print(">")   