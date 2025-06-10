import sys
input = sys.stdin.readline

N= int(input())
store=[0]*(N+1)
def fibo(N):
    store[0]=0
    store[1]=1
    for i in range(2,N+1):
        store[i]=(store[i-1]+store[i-2])
    return store[N]


print(fibo(N))
