# import sys
# sys.stdin = open("input.txt", "r")
from sys import stdin
input=stdin.readline
from collections import deque
queue=deque()
count= int(input())

file=[]
stack=[]
for _ in range(3):
    N,M=map(int, input().split())
    file=list(map(int, input().split()))
    
# def print_queue():
#     while queue:
#         for _ in range(file(len)):
            