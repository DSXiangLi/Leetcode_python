# 给定 n 个非负整数表示每个宽度为 1 的柱子的高度图，计算按此排列的柱子，下雨之后能接多少雨水。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：height = [0,1,0,2,1,0,1,3,2,1,2,1]
# 输出：6
# 解释：上面是由数组 [0,1,0,2,1,0,1,3,2,1,2,1] 表示的高度图，在这种情况下，可以接 6 个单位的雨水（蓝色部分表示雨水）。 
#  
# 
#  示例 2： 
# 
#  
# 输入：height = [4,2,0,3,2,5]
# 输出：9
#  
# 
#  
# 
#  提示： 
# 
#  
#  n == height.length 
#  1 <= n <= 2 * 104 
#  0 <= height[i] <= 105 
#  
#  Related Topics 栈 数组 双指针 动态规划 单调栈 
#  👍 3637 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def trap(self, height: List[int]) -> int:
        total = 0
        stack = [0]
        for i in range(1, len(height)):
            if height[i]< height[stack[-1]]:
                stack.append(i)
            else:
                while stack and height[i] > height[stack[-1]]:
                    mid = stack.pop()
                    if stack:
                        total += (min(height[i], height[stack[-1]]) - height[mid]) * (i-stack[-1]-1)
                stack.append(i)
        return total



# leetcode submit region end(Prohibit modification and deletion)
