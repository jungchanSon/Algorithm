import sys
import math
input = sys.stdin.readline

N = int(input())
arr = list(map(int, input().rstrip().split()))

arr.sort()

l_index = 0
r_index = N-1
ans = [math.inf, []]
while l_index < r_index:
    l_r = arr[l_index] + arr[r_index]
    for i in range(l_index+1, r_index):
        if ans[0] > abs(l_r + arr[i]):
            ans[0] = abs(l_r + arr[i])
            ans[1] = [arr[l_index], arr[i], arr[r_index]]
            
    if l_r >= 0:
        r_index -= 1
    elif l_r < 0:
        l_index += 1
        

print(*ans[1])