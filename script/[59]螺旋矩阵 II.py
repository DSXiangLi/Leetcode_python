# 给你一个正整数 n ，生成一个包含 1 到 n2 所有元素，且元素按顺时针顺序螺旋排列的 n x n 正方形矩阵 matrix 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：n = 3
# 输出：[[1,2,3],[8,9,4],[7,6,5]]
#  
# 
#  示例 2： 
# 
#  
# 输入：n = 1
# 输出：[[1]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= n <= 20 
#  
#  Related Topics 数组 矩阵 模拟 
#  👍 768 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        num = 1
        mat = [[0] * n for i in range(n)]
        left = 0
        right = n - 1
        top = 0
        bottom = n - 1
        while left < right and top < bottom:
            for c in range(left, right):
                mat[top][c] = num
                num += 1
            for r in range(top, bottom):
                mat[r][right] = num
                num += 1
            for c in range(right, left, -1):
                mat[bottom][c] = num
                num += 1
            for r in range(bottom, top, -1):
                mat[r][left] = num
                num += 1

            left += 1
            right -= 1
            bottom -= 1
            top += 1

        if left == right and top == bottom:
            mat[left][top] = num
        elif left == right:
            for r in range(top, bottom + 1):
                mat[r][left] = num
                num += 1
        else:
            for c in range(left, right + 1):
                mat[top][c] = num
                num += 1
        return mat
    # leetcode submit region end(Prohibit modification and deletion)
