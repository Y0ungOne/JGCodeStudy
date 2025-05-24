# 병합 정렬 사용해보기
# 두 개씩 묶은 후 각각각 묶음 안에서 정렬
# 묶여진 묶음을 두 개씩 묶은 후 각각의 묶음 안에서 정렬
# 묶여진 묶음을 두개씩 묶은 후 각각의 묶음 안에서 정렬
# 묶여진 묶음 두 개를 하나로 묶은 후 정렬
# 교재 참고-> 재공부 필요
import sys
from typing import MutableSequence

input = sys.stdin.readline


def MergeSort(a: MutableSequence) -> None:
    n = len(a)
    buff = [None] * n

    def Merge_Sort(a: MutableSequence, left: int, right: int) -> None:
        if left < right:
            center = (left + right) // 2
            Merge_Sort(a, left, center)
            Merge_Sort(a, center + 1, right)
            p = j = 0
            i = k = left

            while i <= center:
                buff[p] = a[i]
                p += 1
                i += 1
            while i <= right and j < p:
                if buff[j] <= a[i]:
                    a[k] = buff[j]
                    j += 1
                else:
                    a[k] = a[i]
                    i += 1
                k += 1

            while j < p:
                a[k] = buff[j]
                k += 1
                j += 1

    Merge_Sort(a, 0, n - 1)
    del buff


if __name__ == "__main__":

    N = int(input())
    arry = []
    for _ in range(N):
        arry.append(int(input()))
    MergeSort(arry)
    for i in arry:
        print(i)
