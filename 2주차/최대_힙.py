# from sys import stdin
# input=stdin.readline
import sys
sys.stdin = open("input.txt","r")
import heapq
heap=[]
N= int(input())

for i in range(N):
    x=int(input())
    if int(x)==0 and len(heap)==0:
        print(0)
    elif int(x)>0:
        heapq.heappush(heap,-x)
    elif int(x)==0:
        print(-heapq.heappop(heap))
        