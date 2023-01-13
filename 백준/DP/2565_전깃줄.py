import sys
input = sys.stdin.readline

n = int(input())
data = [list(map(int, input().split())) for _ in range(n)]
data.sort()
dp = [0 for _ in range(n)]


for i in range(1, n):

    t = data[i][1]
    
    temp = []
    for j in range(0, i):
        if t > data[j][1]:
            temp.append(dp[j])
    if temp:
        dp[i] = max(temp)+1

    
print(n - max(dp)-1)