N= int(input())
a1,a2,a3=1,2,3
K=2**N -1
def Hanoi(N,first_peg,temp_peg,des_peg):

    if N==1:
        # return print(f"{first_peg} {temp_peg}"),print(f"{first_peg} {des_peg}"),print(f"{temp_peg} {des_peg}")
        return print(f"{first_peg} {des_peg}")
    Hanoi(N-1,first_peg,des_peg,temp_peg)    
    Hanoi(1,first_peg,temp_peg,des_peg)
    Hanoi(N-1,temp_peg,first_peg,des_peg)
    

    #n-1개가 1->2 과정을 출력
    #n이 1->3으로 가는걸 출력
    #n-1개가 2->3으로 쌓이는 과정을 출력

if N>=21:
    print(K)
else:
    print(K)
    Hanoi(N,a1,a2,a3)