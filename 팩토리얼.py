N=int(input())
def f(N):
    if N==0 or N==1:
        return 1
    else:
        return f(N-1)*N

print(f(N))