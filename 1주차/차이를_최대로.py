from itertools import permutations
import sys
input=sys.stdin.readline

N=int(input())
arry=[]
arry=(list(map(int, input().split())))


max_result=0

for i in permutations(arry):
    result=0
    for j in range(len(i)-1):
        result+=abs(i[j]-i[(j+1)])
    if result>max_result:
        max_result=result
    
print(max_result)

