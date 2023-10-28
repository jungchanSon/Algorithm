import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr = [0 for _ in range(2000002)]

for _ in range(N):
    a = int(input())
    arr[a+1000000] += 1

for i in range(len(arr)):
    if arr[i]:
        for _ in range(arr[i]):
            print(i-1000000)