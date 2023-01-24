import sys
input = sys.stdin.readline

n, k = map(int, input().rstrip().split())
dp = [ 0 for _ in range(k+1)]
coins = []
for _ in range(n):
    coins.append(int(input()))
coins.sort()
dp[coins[0]] = 1

for i in range(coins[0]+1 , k+1):
    if i % coins[0] == 0:
        dp[i] = 1
        
for i in range(n):
    if i == 0 :
        continue
    for j in range(coins[i], k+1):
        if coins[i] == j : 
            dp[j] += 1
            continue
        temp = j - coins[i]
        dp[j] += dp[temp]
        

# print(dp)
print(dp[-1])
#참고 https://www.youtube.com/watch?v=2IkdAk1Loek