import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [int(input()) for _ in range(N)]
ans = []

arr.sort()
while arr:
    cur = arr.pop(0)
    ans.append(cur * (len(arr) + 1))
    
print(max(ans))