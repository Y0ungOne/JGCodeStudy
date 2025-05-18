C = int(input())
result = 0
arry = []
for i in range(C):
    arry.append(list(map(int, input().split())))
avg_list = []
for i in range(C):
    N = arry[i][0]
    for j in range(1, N + 1):
        result += int(arry[i][j])
    avg = result / N
    avg_list.append(avg)
    result = 0
count_over=0
for i, case in enumerate(arry):
    N = arry[i][0]
    for j in range(1,N + 1):      
        if case[j]>avg_list[i] :
            count_over+=1
    print("%.3f%%" % ((count_over / N) * 100))
    count_over=0