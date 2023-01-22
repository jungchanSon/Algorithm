import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [i for i in range(0, n+1)]

def union(a, b):
    if arr[a] > arr[b] :
        for i in range(len(arr)):
            if arr[i] == arr[a]:
                arr[i] = arr[b]
        arr[b] = arr[a]
    else :
        for i in range(len(arr)):
            if arr[i] == arr[b]:
                arr[i] = arr[a]
        arr[b] = arr[a]

def find(a,b):
    if arr[b] == arr[a]:
        print("YES")
    else :
        print("NO")
for _ in range(m):
    calc, a, b = list(map(int, input().rstrip().split()))
    
    if calc == 0:
        union(a, b)
    else :
        find(a, b)

