N = int(input())
arry = []
for _ in range(N):
    arry.append(int(input()))


def f(n):#n-1, n-2, n-3 의 경우의 수들을 리턴해서 더한 후 리턴 하여 경우의수의 총합을 알려주는 함수수
    if n<0:
        return 0 
    if n == 0:
        return 1
    sumf=0
    if f(n - 1)>0:
        sumf+=f(n-1)
    if f(n - 2)>0:
        sumf+=f(n-2)
    if f(n - 3)>0:
        sumf+=f(n-3)
    
    return sumf


unit = 0
for i in range(len(arry)):
    count=0
    unit = arry[i]
    print(f(unit))
