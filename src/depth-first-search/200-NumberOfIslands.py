class Solution(object):
    def numIslands(self, grid):
        """
        :type grid: List[List[str]]
        :rtype: int
        """
        count = 0
        for row in range(0, len(grid)):
            for col in range(0, len(grid[0])):
                if grid[row][col] == '1':
                    self.dfs(grid, row, col)
                    count += 1
        return count
    
    def dfs(self, grid, row, col):
        if row < 0 or col < 0 or row >= len(grid) or col >= len(grid[0]):
            return
        if grid[row][col] == '0':
            return
        grid[row][col] = '0'
        self.dfs(grid, row - 1, col)
        self.dfs(grid, row + 1, col)
        self.dfs(grid, row, col - 1)
        self.dfs(grid, row, col + 1)

result = Solution().numIslands([
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
])
print(result)


'''

Approach:
1. Loop through each cell using two loops
2. For each cell, we check whether its a land i.e. 1
3. If land, then we pass the cell indexes to dfs for depth First Search
4. In DFS search, we take the given cell and checks for below conditions:
    a. If out of boundary, which means its a water
    b. If its water, we should not consider the cell
5. Mark the cell as visited, by updating it to 0
6. Apply same DFS for cell around the given cell horizontal and vertical adjacent cells. We should not consider diagnol ones.
7. Update the count whenever a cell is completely traversed.
8. Count gives the total number of islands.

'''