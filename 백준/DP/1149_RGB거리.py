import sys
input = sys.stdin.readline

n = int(input().rstrip())
data = []

for _ in range(n):
    d = list(map(int, input().rstrip().split()))
    data.append(d)
    

# dp[n] != dp[n-1]
# r -> g -> r -> b ... 
#시간 초과
"""
answer = -1
def rec(depth, c, sum) :
    global answer
    if depth >= n-1:
        if answer == -1 or sum < answer:
            answer = sum
        return
        
    for i in range(3):
        if i != c:
            rec(depth+1, i, sum+data[depth+1][i])
            
            
for i in range(3):
    rec(0, i, data[0][i])
    
print(answer)
"""



dp =[[0 for _ in range(3)] for _ in range(n)]
# dp[n]r = min(dp[n-1]g , dp[n-1]b)
# dp[1]r = min(dp[0]g, dp[0]b)

for i in range(len(data[0])):
    dp[0][i] = data[0][i]
    
for i in range(1, n):
    dp[i][0] = min(dp[i-1][1], dp[i-1][2]) + data[i][0]
    dp[i][1] = min(dp[i-1][0], dp[i-1][2]) + data[i][1]
    dp[i][2] = min(dp[i-1][0], dp[i-1][1]) + data[i][2]
print(min(dp[n-1][0], dp[n-1][1], dp[n-1][2]))
