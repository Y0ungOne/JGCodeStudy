W, H = map(int, input().split())
t = int(input())
w = [0,W]
h = [0,H]
wh = []

for _ in range(t):
    wh.append(list(map(int, input().split())))

for f,n in wh:
    if f==0:
        h.append(n)
    elif f==1:
        w.append(n)
        
w.sort()
h.sort()

max_w=0
for i in range(len(w)-1):
    max_w=max(max_w, w[i+1] - w[i])

max_h=0     
for i in range(len(h)-1):
    max_h=max(max_h, h[i+1] - h[i])

        
        
print(max_h*max_w)

