import sys
inpu=sys.stdin.readline
N= int(input())
A=list(map(int, input().split()))
N2=int(input())
B=list(map(int, input().split()))


def binary_sort(target, data):
    start=0
    end=len(data)-1
    mid= (start+end)//2
    data.sort()
    if data[mid]>target:
        end=mid-1
    elif data[mid]==target:
        return 1
    else:
        start=mid+1
    return 0

for i in range(len(A)):
    
    if binary_sort(B[i],A)==1:
        print(1)
    else:
        print(0)
    
    

