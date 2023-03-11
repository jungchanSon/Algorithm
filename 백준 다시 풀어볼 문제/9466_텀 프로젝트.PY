import sys
sys.setrecursionlimit(100000)
input = sys.stdin.readline
T = int(input())
def dfs(cur):
    global N
    visited[cur] = 1

    if visited[arr[cur]] == 0:
        dfs(arr[cur])
    elif visited[arr[cur]] == 1:
        index = arr[cur]
        while index != cur:
            N -= 1
            index = arr[index]
        N -= 1
    visited[cur] = -1

for _ in range(T):
    N = int(input())
    arr = [0] + list(map(int, input().rstrip().split()))
    visited = [0 for _ in range(N+1)]

    for i in range(1, 2):
        if visited[i] == 0:    
            dfs(i)
    print(N )
    
    
# 참고 출처.
# 1. for문 조건으로 사이클 체크!! 
# 2. 체크가 끝난 사이클은 Done 배열에 True 처리. (visited[i]: -1 == Done[i]: True )
# 3. Done(visited[i] == -1) == True 이면, 다시 방문할 필요가 없음 => O(n)