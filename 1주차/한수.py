N=int(input())
def H(N):
    if N>=1 and N<=99:
        return N
    else:
        ap=99
        for i in range(100,N+1):
            N_list=list(map(int, str(i).zfill(3)))
            if  N_list[0] - N_list[1] == N_list[1] - N_list[2]:
                ap+=1
        return ap    
print(H(N))