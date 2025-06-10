import sys
input=sys.stdin.readline
arr=[]
initial=input().strip()
parts= initial.split("-")

for part in parts:
    nums=map(int,part.split("+"))
    arr.append(sum(nums))
    
result=arr[0]

for i in range(1,len(arr)):
    result-=arr[i]
print(result)
