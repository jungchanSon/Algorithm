class Solution:
    def matrixScore(self, grid: List[List[int]]) -> int:
        # col
        for i in range(len(grid)):
            if grid[i][0]:
                continue
            for j in range(len(grid[0])):
                grid[i][j] ^= 1

        # row
        for i in range(len(grid[0])):
            cnt = 0
            for j in range(len(grid)):
                cnt += grid[j][i] 
            if cnt * 2 > len(grid):
                continue
            for j in range(len(grid)):
                grid[j][i] ^= 1

        ans = 0
        for i in grid:
            ans += int("".join(map(str, i)) , 2)
        return ans