import sys
input= sys.stdin.readline
# import sys
# sys.stdin = open("input.txt","r")

list_1=list((input().strip()))
list_2=list((input().strip()))
dp=[]
for _ in range(len(list_1)+1):
    dp.append([0] * (len(list_2)+1))


for i in range(len(list_1)):
    for j in range(len(list_2)):
        if list_1[i]==list_2[j]:
            dp[i][j]=dp[i-1][j-1]+1
        else:
            dp[i][j]=max(dp[i-1][j],dp[i][j-1])
            
    
print(dp[i][j])