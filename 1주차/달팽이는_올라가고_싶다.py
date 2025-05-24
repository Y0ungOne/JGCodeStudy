# A,B,V=list(map(int,input().split()))
# stick=0
# day=0
# while True:
#     stick+=A
#     day+=1
#     if stick==V or stick>V:
#         break
#     else:
#         stick-=B
# print(day)
import math
A,B,V=list(map(int,input().split()))

day=math.ceil((V-B)/(A-B))
print(day)