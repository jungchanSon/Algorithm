import sys
import bisect
input = sys.stdin.readline

n, m = map(int, input().rsplit())
arr = []
for _ in range(n):
    arr.append(int(input()))
arr.sort()

st = 0
en = 0
ans = 1e12
while st <= en and st < n and en < n :
    
    if abs(arr[st] - arr[en]) < m:
        en += 1
    elif abs(arr[st] - arr[en]) > m:
        ans = min(ans, abs(arr[st] - arr[en]))
        st += 1
    else:
        print(m)
        quit()
        
print(ans)