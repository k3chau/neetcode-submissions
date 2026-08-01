class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid or not grid[0]:
            return 0
        numIsland = 0
        rows = len(grid)
        cols = len(grid[0])
        def dfs(r,c):
            if(r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]) or grid[r][c] != '1'):
                return
            grid[r][c] = '0'
            dfs(r+1, c)
            dfs(r-1, c)
            dfs(r, c+ 1)
            dfs(r, c - 1)
        for row in range(rows):
            for col in range(cols):
                if grid[row][col] == '1':
                    dfs(row,col)
                    numIsland += 1
                else:
                    continue
        return numIsland
        