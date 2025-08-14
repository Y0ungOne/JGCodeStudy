import sys
input= sys.stdin.readline
# import sys
# sys.stdin = open("input.txt","r")

T=int(input())

for _ in range(T):
    arr=[]
    
    N= int(input())
    for _ in range(N):
        arr.append(list(map(int,input().split())))
    arr.sort()
    passed=arr[0][1]
    count=1
    for i in range(1,N):
        if arr[i][1]<passed:
            passed=arr[i][1]
            count+=1
    print(count)
    