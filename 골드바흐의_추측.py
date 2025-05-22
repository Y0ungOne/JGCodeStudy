import sys
import math


def prime(n):
    if n==2:
        return True
    for j in range(2, int(math.sqrt(n)) + 1):
        if n % j == 0:
            return False
    return True


input = sys.stdin.readline

N = int(input())
arry = []
for _ in range(N):
    arry.append(int(input()))
    
for i in range(N):

    A = B = arry[i] // 2
    for j in range(arry[i] // 2):

        if prime(A) and prime(B):
            print(A, B)
            break
        A -= 1
        B += 1        
