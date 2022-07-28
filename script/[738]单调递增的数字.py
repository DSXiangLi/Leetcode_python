# 当且仅当每个相邻位数上的数字 x 和 y 满足 x <= y 时，我们称这个整数是单调递增的。 
# 
#  给定一个整数 n ，返回 小于或等于 n 的最大数字，且数字呈 单调递增 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: n = 10
# 输出: 9
#  
# 
#  示例 2: 
# 
#  
# 输入: n = 1234
# 输出: 1234
#  
# 
#  示例 3: 
# 
#  
# 输入: n = 332
# 输出: 299
#  
# 
#  
# 
#  提示: 
# 
#  
#  0 <= n <= 109 
#  
#  Related Topics 贪心 数学 
#  👍 274 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def monotoneIncreasingDigits(self, n: int) -> int:
        s=list(str(n))
        l = len(s)
        for i in range(l-1, 0, -1):
            if s[i-1]>s[i]:
                s[i-1] = str(int(s[i-1])-1)
                s[i:] = ['9'] * (l-i)
        return int(''.join(s))
# leetcode submit region end(Prohibit modification and deletion)
