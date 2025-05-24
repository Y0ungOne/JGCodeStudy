import sys

# sys.stdin = open("input.txt","r")
input=sys.stdin.readline
N= int(input())
stack=[]
for _ in range(N):
    arry=list(input().split())
    
    if arry[0]=="push":
        stack.append(arry[1])
    if arry[0]=="pop":
        if not stack:
            print(-1)
        else:
            print(stack.pop())
    if arry[0]=="top":
        if not stack:
            print(-1)
        else:
            print(stack[-1])
    if arry[0]=="size":
        print(len(stack))
    if arry[0]=="empty":
        if not stack:
            print(1)
        else:
            print(0)
            
            