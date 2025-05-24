#한자리수 런타임 에러->배열이 아닌 것으로 바꾸려다가 시간 부족...
N= int(input())    

a=N//10
b=N%10
origin=(a,b)
count=0

def plus(ten,one):
    new_one=(ten+one)%10#두 수를 더해서 %10 한 나머지를 다음 수의 1의자리에 넣을 거임
    new_ten=one
    return new_ten,new_one #1의자리 수 였던 b를 10의자리 위치(앞)에 넣음, 1의자리(뒷자리)에 s값 넣음

#a,b를 origin 값과 비교하기 위해선 한번 바뀌어야함-> 한번 while문 밖에서 실행 함
a,b+=plus(a,b) #a,b를 활용하여 도출된 10의자리 값과 1의자리 값을 다시 a,b라는 변수에 넣어줌 그래서 origin과 다른지 비교 할 수 있음 
count+=1

while (a,b)!=origin: #새로 a,b자리에 들어온 b,s값이 origin에 저장되어있던 a,b의 값과 같은지 확인해서 같지 않다면 while 반복문 진행
    a,b=plus(a,b)
    count+=1

print(count)