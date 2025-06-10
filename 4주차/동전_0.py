import sys
input=sys.stdin.readline

N,K=map(int,input().split())

coin=[]
for _ in range(N):
    coin.append(int(input()))
coin.reverse()

cnt=0
for i in coin :
    cnt+=K//i
    K=K%i

print(cnt)