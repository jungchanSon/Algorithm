import sys
from collections import deque
input = sys.stdin.readline

n, s = map(int, input().rsplit())
arr = list(map(int, input().rsplit()))
ans = 0
def rec(pos, c):
    global ans
        
    if pos == n:
        if c == s:
            ans += 1
        return
    
    rec(pos+1, c+arr[pos])
    rec(pos+1, c)

rec(0, 0)
if s == 0:
    ans -=1
print(ans)