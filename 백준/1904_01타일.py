import sys

input = sys.stdin.readline

n = int(input().rstrip())

if n == 1:
    print(1)
    quit()
elif n == 2:
    print(2)
    quit()
    
dp = [0 for _ in range(n)]
dp[0] = 1
dp[1] = 2

for i in range(2, n):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746 

# dp[i-1] % 15746으로 출력하면 에러 
# => 나머지 수로 출력하는 문제들은 나머지 연산 후 작은 값으로 배열에 저장.
print(dp[n-1] )