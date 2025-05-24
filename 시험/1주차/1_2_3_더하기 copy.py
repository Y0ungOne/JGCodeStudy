N = int(input())
arry = []
for _ in range(N):
    arry.append(int(input()))
count = 0

def f(n):#생기는 경우의 수 마다 count가 +1이 되어서 총 합을 리턴할 수 있는 방법
    global count
    if n<0:
        return  
    if n == 0:
        count +=1
        return 
    if f(n - 1)>0:
        f(n-1)
    if f(n - 2)>0:
        f(n-2)
    if f(n - 3)>0:
        f(n-3)
    
    return


unit = 0
for i in range(len(arry)):
    count=0
    unit = arry[i]
    f(unit)
    count += 1
    print(count)
