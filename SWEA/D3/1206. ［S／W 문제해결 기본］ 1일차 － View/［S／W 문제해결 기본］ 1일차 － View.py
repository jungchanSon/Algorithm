import math

# T = int(input())
T = 10
for test_case in range(1, T + 1):
    n = int(input())
    ans = 0
    arr = list(map(int, input().rsplit()))
    l = 2
    r = n-2
    while l < r:
        c = l
        left = max(arr[c-1], arr[c-2])
        right = max(arr[c+1], arr[c+2])
        
        mx = max(left, right)
        tmp = arr[c] - mx
        if tmp > 0: ans += tmp
        
        l += 1
    print(f"#{test_case} {ans}")