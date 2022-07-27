# 给你一个 m x n 的矩阵 board ，由若干字符 'X' 和 'O' ，找到所有被 'X' 围绕的区域，并将这些区域里所有的 'O' 用 'X' 填充
# 。
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X"
# ,"X"]]
# 输出：[["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# 解释：被围绕的区间不会存在于边界上，换句话说，任何边界上的 'O' 都不会被填充为 'X'。 任何不在边界上，或不与边界上的 'O' 相连的 'O' 最终都
# 会被填充为 'X'。如果两个元素在水平或垂直方向相邻，则称它们是“相连”的。
#  
# 
#  示例 2： 
# 
#  
# 输入：board = [["X"]]
# 输出：[["X"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  m == board.length 
#  n == board[i].length 
#  1 <= m, n <= 200 
#  board[i][j] 为 'X' 或 'O' 
#  
#  
#  
#  Related Topics 深度优先搜索 广度优先搜索 并查集 数组 矩阵 
#  👍 830 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def solve(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        nrow = len(board)
        ncol = len(board[0])
        stack = []
        for i in range(ncol):
            if board[0][i] == 'O':
                stack.append((0, i))
            if board[nrow - 1][i] == 'O':
                stack.append((nrow - 1, i))
        for i in range(nrow):
            if board[i][0] == 'O':
                stack.append((i, 0))
            if board[i][ncol - 1] == 'O':
                stack.append(((i, ncol - 1)))
        while stack:
            node = stack.pop()
            board[node[0]][node[1]] = 'M'
            for nr,nc in [(node[0]+1, node[1]),(node[0]-1,node[1]), (node[0],node[1]+1), (node[0],node[1]-1)]:
                if nr < nrow and nr>=0 and nc<ncol and nc>=0 and board[nr][nc]=='O':
                    stack.append((nr,nc))

        for i in range(nrow):
            for j in range(ncol):
                if board[i][j] =='M':
                    board[i][j] = 'O'
                elif board[i][j]=='O':
                    board[i][j] = 'X'
# leetcode submit region end(Prohibit modification and deletion)
