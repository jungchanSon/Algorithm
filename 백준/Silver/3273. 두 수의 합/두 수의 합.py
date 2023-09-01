import sys
input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().rsplit()))
x = int(input())

arr.sort()

l = 0
r = n -1
ans = 0
while l < r:
    s = arr[l] + arr[r]
    if s == x:
        ans += 1 
        l += 1
        r = n-1
    elif s > x:
        r -= 1
    else:
        l += 1 
print(ans)