num = int(input())
# arry = []
# for _ in range(num):
#     arry.append(input())
quiz_set=[input() for _ in range(num)]
for answer in quiz_set:
    result=0
    rate=1
    for i in answer:
        if i=="O":
            result+=rate
            rate+=1
        else:
            rate=1
    print(result)    