import sys
from collections import deque
# sys.stdin = open("input.txt","r")
input=sys.stdin.readline
N= int(input().rstrip())
queue=deque()
for _ in range(N):
    arry=list(input().rstrip().split())
    
    if arry[0]=="push":
        queue.append(arry[1])
    elif arry[0]=="pop":
        if not queue:
            print(-1)
        else:
            print(queue.popleft())
    elif arry[0]=="front":
        if not queue:
            print(-1)
        else:
            print(queue[0])
    elif arry[0]=="back":
        if not queue:
            print(-1)
        else:
            print(queue[-1])
    elif arry[0]=="size":
        print(len(queue))
    elif arry[0]=="empty":
        if not queue:
            print(1)
        else:
            print(0)
            
            