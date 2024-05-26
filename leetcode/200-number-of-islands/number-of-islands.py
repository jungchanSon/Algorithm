from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        n, m = len(grid), len(grid[0])
        ans = 0
        dx = [0, 0, -1, 1]
        dy = [-1, 1, 0, 0]
        for i in range(n):
            for j in range(m):
                print(i, j)
                if grid[i][j] == "1":
                    q = deque([[i, j]])
                    grid[i][j] = "0"
                    ans += 1
                    while q:
                        cy, cx = q.popleft()
                        
                        for k in range(4):
                            nx = dx[k] + cx
                            ny = dy[k] + cy
                            if ny < 0 or ny >= n or nx < 0 or nx >= m:
                                continue
                            if grid[ny][nx] == "1":
                                grid[ny][nx] = "0"
                                q.append([ny, nx])

        return ans