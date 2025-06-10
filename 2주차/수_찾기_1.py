import sys
input=sys.stdin.readline
N= int(input())
A=list(map(int, input().split()))
N2=int(input())
B=list(map(int, input().split()))

A.sort()

def binary_sort(target, data):
    start=0
    end=len(data)-1
    while start<=end:
        mid= (start+end)//2
    
        if data[mid]>target:
            end=mid-1
        elif data[mid]==target:
            return True
        else:
            start=mid+1
    return False 

for i in range(len(B)):
    
    if binary_sort(B[i],A)==True:
        print(1)
    else:
        print(0)