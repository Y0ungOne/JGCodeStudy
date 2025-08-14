import sys
input=sys.stdin.readline
# import sys
# sys.stdin = open("input.txt","r")

n=int(input())

if n==0 or n==1 or n==3: # 이 값들 만나면 아래 실행 없이 끝내도록 
    print(-1)
    sys.exit()
elif n==2 or n==5:
    print(1)
    sys.exit()
dp=[0]*(n+1) # 배열 초기화
dp[0]=-1     # 초기값 설정
dp[1]=-1
dp[2]=1
dp[3]=-1
for i in range(4,n+1): # dp 실행
    if i%5==0:
        dp[i]=i//5
    else:
        dp[i]=dp[i-2]+1    
print(dp[i])