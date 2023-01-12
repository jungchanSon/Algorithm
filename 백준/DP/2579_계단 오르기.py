import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = [int(input().rstrip()) for _ in range(n)]

#연속 3개 x / 한번에 1개, 2개 / 마지막은 꼭 밟아야함 .
#dp[n] = max(dp[n-1], dp[n-2])

dp = [ 0 for _ in range(n)]

if n == 1:
    print(data[0])
    quit()
elif n == 2:
    print(data[0] + data[1])
    quit()
    
dp[0] = data[0]
dp[1] = data[0]+data[1]
for i in range(2, n):
    
    if i == 2 : # 3번 계단
        dp[i] = max(data[0], data[1]) + data[i]
    else:
        # 직전 밟고,
        a = dp[i - 3]+data[i-1]
        # 직전 안밟고,
        b = dp[i -2]
        dp[i] = max(a, b) + data[i] 

print(dp[-1])
"""
반례 : 3 10 20 30 -> IF 3 추가
"""
"""
6
10
20
15
25
10
20
"""

