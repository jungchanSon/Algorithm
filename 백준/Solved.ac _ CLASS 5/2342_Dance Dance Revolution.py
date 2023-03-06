import sys
input = sys.stdin.readline

arr = list(map(int, input().rstrip().split()))
l = arr[0]
r = 0

ll = arr[0]
rr = 0

# 왼발, 오른발
dp = [[0, 0] for _ in range(len(arr))]
dp[0] = [2, 2]

# 바텀업
for i in range(1, len(arr)):
    print(l , r)
    # 왼발
    prev = min(dp[i-1][0], dp[i-1][1])
    # if prev == dp[i-1][0]:
        
    # if prev == dp[i-1][1]:
    if l == arr[i]:
        dp[i][0] = prev + 1
    elif abs(l-arr[i]) == 1 or abs(l-arr[i]) == 3:
        dp[i][0] = prev + 3
    elif abs(l-arr[i]) == 2:
        dp[i][0] = prev + 4  
    
    if r == 0:
        if l != r:
            dp[i][1] = prev +2
            r = arr[i]
    else:
        if r == arr[i]:
            dp[i][1] = prev + 1
        elif abs(r - arr[i]) == 1 or abs(r - arr[i]) == 3:
            dp[i][1] = prev + 3
        elif abs(r - arr[i]) == 2:
            dp[i][1] = prev + 4
    if dp[i][0] < dp[i][1]:
        l = arr[i]
    else:
        r = arr[i]
        

    
print(min(dp[len(arr)-3]))
print(dp)
"""
dp[n] = dp[n-1] + min(l, r)
같은 지점 : 1
중앙 -> 다른 : 2
인접 -> : 3
반대 -> : 4
"""