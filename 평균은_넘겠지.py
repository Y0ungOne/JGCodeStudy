C = int(input())
result = 0
arry = []
for i in range(C):
    arry.append(list(map(int, input().split())))
avg_list = []
for i in range(C):
    N = arry[i ][0]
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
    
#우진님 코드드
# n = int(input())
# for _ in range(n):
#     data = list(map(int, input().split()))
#     number = data[0]  # 단일 변수에는 복수형 변수명 쓰지말자...
#     scores = data[1:]
#     average = sum(scores) / number
#     good_scores = [i for i in scores if i >= average]
#     ratio = len(good_scores) / number * 100
#     print(f"{ratio:.3f}%")  # 소숫점 자리수 고정법 : f-string에서 :자릿수f