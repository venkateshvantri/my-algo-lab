class Solution(object):
    def closedIsland(self, nums):
        """
        :type nums: List[List[int]]
        :rtype: int
        """

        count = 0

        for i in range(0, len(nums)):
            for j in range(0, len(nums[0])):

                res = 0
                if(nums[i][j] == 0):
                    res = self.dfs(nums,i,j, res)
                    if(res == 0):
                        count += 1

        return count

    
    def dfs(self,nums, i, j, res):
        if(nums[i][j] == 1):
            return res + 0
        if(i-1 < 0 or j-1 < 0 or i+1 >= len(nums) or j+1 >= len(nums[0])):
            return res + 1
            

        print(i,j)        
        nums[i][j] = 1
        res = self.dfs( nums, i+1, j, res)
        res = self.dfs( nums, i-1, j, res)
        res = self.dfs( nums, i, j+1, res)
        res = self.dfs( nums, i, j-1, res)

        return res
        

result = Solution().closedIsland([[0,0,0,1,0],[0,0,1,0,1],[0,1,1,1,0]])
print(result)

'''

1254. Number of Closed Islands
Medium

Given a 2D grid consists of 0s (land) and 1s (water).  An island is a maximal 4-directionally connected group of 0s and a closed island is an island totally (all left, top, right, bottom) surrounded by 1s.

Return the number of closed islands.

***********************************************************************************************************************************************

Example 1:

Input: grid = [[1,1,1,1,1,1,1,0],[1,0,0,0,0,1,1,0],[1,0,1,0,1,1,1,0],[1,0,0,0,0,1,0,1],[1,1,1,1,1,1,1,0]]
Output: 2
Explanation: 
Islands in gray are closed because they are completely surrounded by water (group of 1s).
Example 2:

Input: grid = [[0,0,1,0,0],[0,1,0,1,0],[0,1,1,1,0]]
Output: 1
Example 3:

Input: grid = [[1,1,1,1,1,1,1],
               [1,0,0,0,0,0,1],
               [1,0,1,1,1,0,1],
               [1,0,1,0,1,0,1],
               [1,0,1,1,1,0,1],
               [1,0,0,0,0,0,1],
               [1,1,1,1,1,1,1]]
Output: 2

Constraints:

1 <= grid.length, grid[0].length <= 100
0 <= grid[i][j] <=1

***********************************************************************************************************************************************

Approach:
- Use DFS
- Loop through each cell from left-right and top-botton
- if a given cell has 0, 
    - Mark the cell as visited by turning it to 1
    - then make a recursive call for cells around it i.e. left, right, top and botton
    - Check whether the dfs traversal is falling outside the boundary, 
        - if yes then we ignore that island 
        - if no, we got a closed island
- Ignore the cells with below conditions during recursion
    - If a cell has 1 (OR)
    - if a cell is falling outside the boundary

'''