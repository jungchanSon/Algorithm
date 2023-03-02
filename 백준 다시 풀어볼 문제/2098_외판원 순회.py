import sys
import math
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[ math.inf for _ in range(1 << N)] for _ in range(N)]

def dfs(start, visited):
    print(visited)
    if visited == (1 << N) - 1:
        if graph[start][0]:
            return graph[start][0]
        else:
            return math.inf
        
    if dp[start][visited] != math.inf:
        return dp[start][visited]
        
    for i in range(1, N):
        if not graph[start][i] or visited & (1 << i) :
            continue
        
        dp[start][visited] = min(dp[start][visited], dfs(i, visited | (1 << i)) + graph[start][i])

    return dp[start][visited]

print(dfs(0, 1))

# 참고 : https://hongcoding.tistory.com/83