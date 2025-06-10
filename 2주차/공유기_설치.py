from sys import stdin
input=stdin.readline
# import sys
# sys.stdin = open("input.txt","r")
house=[]
N,C=list(map(int, input().split()))
for i in range(N):
    house.append(int(input()))
house.sort()

def binary(house):
    result = 0
    min_v = 1  # 공유기 사이 최소 거리 (0은 의미 없음)
    max_v = house[-1] - house[0]  # 공유기 사이 최대 거리

    while(min_v<=max_v):
        count=1 
        now=house[0]
        ml=(min_v+max_v)//2
        
        for j in range(1,len(house)):
            if house[j] - now >= ml:
                count+=1
                now=house[j]

        if count>=C:
            result = ml
            min_v=ml+1
        else:
            max_v=ml-1
    
    return result
print(binary(house))
