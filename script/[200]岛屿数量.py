# 给你一个由 '1'（陆地）和 '0'（水）组成的的二维网格，请你计算网格中岛屿的数量。 
# 
#  岛屿总是被水包围，并且每座岛屿只能由水平方向和/或竖直方向上相邻的陆地连接形成。 
# 
#  此外，你可以假设该网格的四条边均被水包围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# 输出：1
#  
# 
#  示例 2： 
# 
#  
# 输入：grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# 输出：3
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == grid.length 
#  n == grid[i].length 
#  1 <= m, n <= 300 
#  grid[i][j] 的值为 '0' 或 '1' 
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 1816 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        def dfs(row, col):
            for x,y in ([row-1,col], [row+1,col],[row, col-1],[row,col+1]):
                if x>=0 and x<nrow and y>=0 and y<ncol and grid[x][y]=='1':
                    grid[x][y]=2
                    dfs(x, y)
            return

        nrow = len(grid)
        ncol = len(grid[0])
        total = 0
        for i in range(nrow):
            for j in range(ncol):
                if grid[i][j]=='1':
                    total+=1
                    dfs(i,j)
        return total

# leetcode submit region end(Prohibit modification and deletion)
