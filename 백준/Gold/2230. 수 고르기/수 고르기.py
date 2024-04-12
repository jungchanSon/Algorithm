import sys
import math

input = sys.stdin.readline 
N, M = map(int,input().rsplit())
arr = [int(input()) for _ in range(N)]
arr.sort()
ans = math.inf 
if N <= 1:
    print(0)
if N <= 2:
    print (arr[1] - arr[0])
else: 
    l, r = 0, 1
    while l <= r and r < N:
        
        res = arr[r] - arr[l]
        if res == M:
            ans = res 
            break
        elif res > M:
            l += 1
            ans = min(ans, res)
        elif res < M:
            r += 1 
            
    print(ans)