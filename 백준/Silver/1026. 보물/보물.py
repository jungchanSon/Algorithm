import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
arr1 = list(map(int, input().rsplit()))
arr2 = list(map(int, input().rsplit()))
arr3 = sorted(arr2, reverse=True)
ans = 0

arr1.sort()

for i in range(N):
    ans += arr1[i] * arr3[i]

print(ans)