import sys
import math
input = sys.stdin.readline

N, S = map(int, input().rstrip().split())
arr = list(map(int, input().rstrip().split()))
ans = math.inf

# dp 누접합 완전탐색 -> 시간 초과.

# dp = [0 for _ in range(N)]
# dp[0] = arr[0]

# for i in range(1,N):
#     dp[i] = dp[i-1] + arr[i]

# for i in range(N):
#     if dp[i] >= S:
#         ans = i+1
#         break
    
# if ans == math.inf:
#     print(0)

# for i in range(1, N):
#     for j in range(i, N):
#         if dp[j] - dp[i-1] >= S:
#             ans = min(ans, j-i+1)

arr.append(0)
start = 0
end = 0
current_sum = arr[0]

while start <= end and end < N:
    if current_sum < S:
        end += 1
        current_sum += arr[end]
    else:
        ans = min(ans, end-start+1)
        
        current_sum -= arr[start]
        start += 1
if ans == math.inf:
    print(0)
else:
    print(ans)