import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()

dp = [0 for _ in range(n)]


for i in range(1, len(data)):
    
    s = data[i][0]
    e = data[i][1]
    
    for j in range(0, i):
        if s < data[j][0] and e < data[j][1]:
            dp[i] = max(dp[i], dp[j])
        elif s > data[j][0] and e > data[j][1]:
            dp[i] = max(dp[i], dp[j])
    dp[i] += 1
print(n - len(dp))