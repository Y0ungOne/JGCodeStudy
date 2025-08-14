import sys 
input= sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    coin = list(map(int, input().split())) #지난 문제와 달리 최소한의 동전 사용이 아니기에 reverse필요 없음
    M=int(input())
    
    dp=[0]*(M+1)# 배열 초기화
    dp[0]=1 # dp[i]는 금액 i를 만드는 방법의 수-> 0원 만드는건 아무것도 않넣는 1가지 방법이 있음
    
    for i in coin : # coin 배열안에 들어잇는 동전들로 금액 i를 만들 수 있는 방법: i-coin원을 만들 수 있는 방법에 coin을 하나씩 추가
        for j in range(i,M+1):
            dp[j]+=dp[j-i] #2원을 만드는 방버에 2원을 더하면 4원
    print(dp[M])
    