import sys
from collections import deque
input = sys.stdin.readline

n, m = map(int, input().rsplit())

arr = [True for _ in range(1000001)]
arr[1] = False
cur = 1
for i in range(2, len(arr)):
    for j in range(i*i, len(arr), i):
        arr[j] = False

for i in range(n, m+1):
    if arr[i]:
        print(i)