arry=[]
for i in range(9):
    num=int(input()) 
    arry.append(num)

print(max(arry))
print(arry.index(max(arry))+1)