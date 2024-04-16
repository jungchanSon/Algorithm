import sys
from collections import deque

input = sys.stdin.readline

n = int(input())
a = 0
b = 1
ans = 0
if n == 1:
    print(1)
    quit()
    
while a <= n:
    a += b
    ans += 1
    b += 1
print(ans-1)