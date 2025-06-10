import sys
sys.stdin = open("input.txt", "r")
# from sys import stdin
# input=stdin.readline
from collections import deque
result=[]
arr=input()
keyword=input()
L=len(keyword)
queue=deque()
for i in range(len(arr)):
    queue.append(arr[i])

while queue:
    for j in range(len(arr)):
        result.append(queue[j])
        search_keyword=result[j:L+1]
        if search_keyword==keyword:
            queue.append(queue.popleft)
        
