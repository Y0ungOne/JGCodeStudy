# 풀지 못했습니다. 
# 그냥 넘어가시면 됩니다
import sys
sys.stdin = open("input.txt","r")
# import sys
# input=sys.stdin.readline
arr=[]
n=int(input())
for _ in range(n):
    arr.append(list(map(int,input().split())))
jump=arr[0][0]
cnt=1
while(jump!=arr[n][n]):
    arr[0+jump][0]