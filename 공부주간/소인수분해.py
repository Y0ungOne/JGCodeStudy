import sys
input= sys.stdin.readline
# import sys
# sys.stdin = open("input.txt","r")

N= int(input())
n=N
a=2
for i in range (N):
    if n%a==0:
        print (a)
        n=n/a
        
    else:
        a+=1

# 내가 받은 n을 2부터 나눠봄
# 2로 나눈 나머지가 0 이면 2 출력
# 2로 나눈 결과값에 다시 한번 2 나눔
# 2로 나눠지지 않으면 나누는 수 1 증가 -> 3으로 나눠봄
# 3으로 나눠지지 않으면 나누는 수 1 증가 -> 반복
# 나누는 수가 자기자신인 n까지 나눠봤으면 종료
# N=int(input())
# a=2
# n=N
# while(a==N):
#     if n%a==0:
#         print(a)
#         n=n/a
#     else:
#         a+=1
