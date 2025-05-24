N=int(input())
arry=[]
for _ in range(N):
    arry.append(input())

# arry.sort()
# arry.sort(key=len)
arry.sort(key=lambda x:(len(x),x))
dict_arry=dict.fromkeys(arry)

dict_arry=list(dict_arry)
for i in dict_arry:
    print(i)
    

# data.sort(key="pick")
# def pick(x):
#     return (len(x),x)

# x= ["이름",11]