#도수정렬 사용해서 문제 풀기
import sys
input=sys.stdin.readline
print=sys.stdout.write

N=int(input())

arry=[0]*10001

for i in range(N):
    arry[int(input())]+=1
    
for i in range(1,10001):
    for j in range(arry[i]):
        print(str(i)+"\n")



# arry 안의 값을 검사, 해당 값의 count_arry 인덱스 값을 +1
