import sys

input = sys.stdin.readline

n = int(input().rstrip())
numbers = list(map(int, input().rstrip().split()))

dp = []

for i in range(n):
    dp.append(numbers[i])
    
for i in range(1, n):
    dp[i] = max(dp[i-1] + numbers[i], numbers[i])

print(max(dp))