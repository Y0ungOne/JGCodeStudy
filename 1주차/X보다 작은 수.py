N,X=list(map(int,input().split()))
arry=list(map(int,input().split()))
new_arry=[i for i in arry if i<X]
for i in new_arry:
    print(i,end=" ")
    