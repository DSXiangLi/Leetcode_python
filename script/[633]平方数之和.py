# 给定一个非负整数 c ，你要判断是否存在两个整数 a 和 b，使得 a² + b² = c 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：c = 5
# 输出：true
# 解释：1 * 1 + 2 * 2 = 5
#  
# 
#  示例 2： 
# 
#  
# 输入：c = 3
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= c <= 2³¹ - 1 
#  
#  Related Topics 数学 双指针 二分查找 👍 372 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        left = 0
        right = int(c**0.5)
        while left<=right:
            if left**2 + right**2 ==c:
                return True
            elif left**2 + right**2 > c:
                right-=1
            else:
                left+=1
        return False
# leetcode submit region end(Prohibit modification and deletion)
