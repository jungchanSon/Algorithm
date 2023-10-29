import sys
import bisect

input = sys.stdin.readline

n = int(input())
arr = []
for _ in range(n):
    arr.append(int(input()))
    
ans = 0
arr.sort()
sums = []
for i in range(n):
    for j in range(i, n):
        sums.append(arr[i]+arr[j])

sums.sort() 
for i in range(n-1, -1, -1):
    for j in range(0, i):
        target = arr[i] - arr[j]
        l = bisect.bisect_left(sums, target, 0, len(sums))
        r = bisect.bisect_right(sums, target, 0, len(sums))
    
        if r - l > 0:
            print(arr[i])
            quit()