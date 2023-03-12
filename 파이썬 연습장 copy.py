import sys
input = sys.stdin.readline

# 초기화 시작
N = int(input())
arr = [0] + list(map(int, input().rstrip().split()))
sums = [ 0 for _ in range(N+1)]
dp = [0 for _ in range(N+1)]
ans = 0

if N == 1:
    print(1)
    quit()
sums[1] = arr[1]
dp[1] = 1 
#  초기화 끝

# DP 시작
for i in range(1, N+1):
    if sums[i] == arr[i]:
        dp[i] = 1 
    for j in range(i-1, 0, -1):
        if sums[j] >= arr[i]:
            if dp[j]+1 > dp[i]:
                dp[i] = dp[j] + 1
                sums[i] = sums[j] + arr[i]
    if sums[i] == 0:
        sums[i] = arr[i]
        dp[i] = 1 
# 끝
print(arr)
print(sums)
print(dp)
print(dp[N])
"""
7
        1 2 1 5 3 4 10
누적합  1 2 3 5 6 10 20
DP      1 1 2 1 3 4  5 

arr : 각 도미노 값
sum : 누적합
DP  : 옳은 순서 도미노

arr[n] <= sum[i] and dp[i] > dp[n]
=
sum[n] = sum[i] + arr[n]  
dp[n] = dp[i] + 1
"""