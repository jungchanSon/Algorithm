import sys
import math
input = sys.stdin.readline

N = int(input())
graph = [list(map(int, input().rstrip().split())) for _ in range(N)]
dp = [[ -1 for _ in range(1 << N)] for _ in range(N)]

def dfs(start, visited):
    if visited == (1 << N) - 1:
        if graph[start][0] :
            dp[start][visited] = graph[start][0]
            return graph[start][0]
        else:
            return math.inf
        
    if dp[start][visited] != -1:
        return dp[start][visited]
    
    mm = math.inf
    for i in range(N):
        if visited & (1 << i):
            continue
        if not graph[start][i]:
            continue 
        
        mm = min(mm, dfs(i, visited | (1 << i)) + graph[start][i])
    dp[start][visited] = mm
    return dp[start][visited]

print(dfs(0, 1))

# 참고 : https://hongcoding.tistory.com/83
# 시간초과 -> dp를 -1로 초기화 : https://www.acmicpc.net/board/view/
#                                https://yiyj1030.tistory.com/488