import sys
import bisect
input = sys.stdin.readline

n, s = map(int, input().rsplit())

arr = list(map(int, input().rsplit()))

ans =  1e10
sums = 0

st = 0
en = 0
f = False
while st <= en and st < n and en <= n:
    
    if sums < s:
        if en == n:
            break
        sums += arr[en]
        en += 1
    elif sums >= s:
        ans = min(ans, en-st)
        sums -= arr[st]
        st += 1
        f = True
        
if f:
    print(ans)
else:
    print(0)