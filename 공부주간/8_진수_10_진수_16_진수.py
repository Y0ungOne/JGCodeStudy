import sys
input= sys.stdin.readline
# import sys
# sys.stdin = open("input.txt","r"
X=input()
arr=str(X)
if arr[0]=='0' and arr[1]=='x':
    print(int(arr,16))

elif arr[0]=='0' and arr[1]!='x':
    print(int(arr,8))
else:
    print(X)
    
# 첫 줄에 X를 입력받음
# 이건 정수고 수의 앞의 0으로 시작하면 8진수, 0x로 시작하면 16진수 이외의 경우는 10진수
# 출력형태는 10진수
# 앞이 0으로 시작하면
# 


