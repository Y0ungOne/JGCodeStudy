h=[]
h_sum=0
for _ in range(9):
    h.append(int(input()))
h.sort()
for i in h:
    h_sum+=i
rest= h_sum-100
for i in range(len(h)):
    for j in range(1,len(h)-1):
        if h[i]+h[j]==rest:
            fake1=h[i]
            fake2=h[j]
            break
            
h.remove(fake1)
h.remove(fake2)
for i in h:
    print(i)