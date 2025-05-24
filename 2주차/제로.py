import sys

# sys.stdin = open("input.txt","r")
input=sys.stdin.readline
N= int(input())
stack=[]
for _ in range(N):
    num= int(input())
    if num>0:
        stack.append(num)
    if num==0:
        stack.pop()  
result=0    
for i in range(len(stack)):
    result+=stack[i]
    
print(result)