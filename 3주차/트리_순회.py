import sys
input= sys.stdin.readline
# import sys
# sys.stdin = open("input.txt","r")
N= int(input())
arr={}
for _ in range(N):
    root, left, right= input().split()
    arr[root]=[left, right]

def preorder(node):
    if node==".":
        return
    print(node, end='')
    preorder(arr[node][0])
    preorder(arr[node][1])

def inorder(node):
    if node==".":
        return
    inorder(arr[node][0])
    print(node, end='')
    inorder(arr[node][1])
    
def postorder(node):
    if node==".":
        return
    postorder(arr[node][0])
    postorder(arr[node][1])
    print(node, end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()