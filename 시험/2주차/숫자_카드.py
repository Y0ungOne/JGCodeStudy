# import sys
# sys.stdin = open("input.txt", "r")
from sys import stdin
input=stdin.readline
result=[]
N= int(input())
arr=list(map(int, input().split()))
    
M= int(input())
com=list(map(int, input().split()))
arr.sort()

    
def binary(data, target):
    left=0
    right=len(data)-1
    while(left<=right):

        mid=(left+right)//2
        if data[mid]==target:
            return True
        elif target>data[mid]:
            left=mid+1
        elif target<data[mid]:
            right=mid-1
    return False 
    
    

for i in com:
    if binary(arr,i)==True:
        result.append(1)

    else:
        result.append(0)

for j in range(len(result)):
    print(f'{result[j]} ',end='')