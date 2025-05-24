from itertools import combinations

N, S = map(int, input().split())
arry=[]
arry=list(map(int, input().split()))
count=0
for r in range(1, N+1):  # 부분수열은 공집합 제외하기 위해서 1부터 시작(공집합이 아닌 배열의 요소가 1개인 것부터 검사하자!)
    for comb in combinations(arry, r): # 조합 하나를 의마하는 내용-> combination으로 만든 조합중 첫번째부터 S랑 같은지 검사하기 위한 시작
        if sum(comb) == S: #그 조합들의 합이 S와 같다면 카운트 증가시키는 중
            count += 1
print(count)