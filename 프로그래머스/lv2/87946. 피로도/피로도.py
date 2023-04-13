def solution(k, dungeons):
    ans = []
    visited = [False for _ in range(len(dungeons))]
    print(visited)
    def dfs(current, depth):
        for i in range(len(dungeons)):
            if visited[i]:
                continue
            if dungeons[i][0] >current:
                continue
            visited[i] = True
            dfs(current-dungeons[i][1], depth+1)
            visited[i] = False
        ans.append(depth)
    dfs(k, 0)
    return max(ans)