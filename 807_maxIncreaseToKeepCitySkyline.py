class Solution:
    def maxIncreaseKeepingSkyline(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        rowLen = len(grid)
        colLen = len(grid[0])
        topView = []
        sideView = []
        col = 0
        result = 0
        for row in grid:
            sideView.append(max(row))
            topView.append(max(Solution.getCol(grid, col)))
            col += 1
        row = 0
        while (row < rowLen):
            col = 0
            while (col < colLen):
                result += (min(sideView[row], topView[col]) - grid[row][col])
                col += 1
            row += 1
        return result
		
		
    def getCol(grid, colNo):
        col = []
        row = 0
        rowLen = len(grid)
        while (row < rowLen):
            col.append(grid[row][colNo])
            row += 1
        return col
