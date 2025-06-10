import sys
input= sys.stdin.readline
# sys.stdin = open("input.txt","r")
N= int(input())
arry= []

#괄호 검사 함수->메인 함수의 arry안에 괄호뭉텅이를 요소로 하는 배열을 받음
def PS(data):
    #괄호 뭉텅이 하나를 담은 배열 선언 및 초기화 하는 배열->다음 뭉터기도 검사해야해서 초기화 해야함
    list_ps=[]
    
    for j in data:  #괄호 뭉텅이검사
        
        #첫번째로 들어오는 요소가 )면 또는, 배열에 요소가 들어오지 않았는데 )시작이면 False리턴 
        if len(list_ps)==0 and j==")":
            return False
        
        #이제 첫 요소가 )이 아닐때가 확실하기 때문에 열림 들어오면 괄호 하나 담기
        if j=="(":
            list_ps.append(j)
        #)가 들어오면 열림 하나 pop
        if j==")":
            list_ps.pop()
            
    #뭉텅이를 다 검사했을때 사실 완전하려면 배열에 남아있는게 없어야함 따라서 길이가 0일때 True 리턴
    if len(list_ps)==0:
        return True
    
    #배열에 뭔가 남아있다면 괄호가 온전하지 않았다는 것-> False 리턴
    else:
        return False

#메인 함수에서 arry를 N번입력 받고       
for i in range(N):
    arry.append(list(input()))
    
    #arry의 요소마다 리턴값을 검사하여 True면 YES, False면 NO출력
    if PS(arry[i])==True:
        print("YES")
    else:
        print("NO")