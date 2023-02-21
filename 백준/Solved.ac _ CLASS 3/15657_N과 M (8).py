import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))

arr.sort()
def bt(i, depth, l):
    if depth == M:
        print(*l)
        return
   
    for j in range(i, len(arr)):
        bt(j, depth+1, l+[arr[j]])

for i in range(N):
    bt(i, 1, [arr[i]])