# 给定一个非空字符串 s，最多删除一个字符。判断是否能成为回文字符串。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: s = "aba"
# 输出: true
#  
# 
#  示例 2: 
# 
#  
# 输入: s = "abca"
# 输出: true
# 解释: 你可以删除c字符。
#  
# 
#  示例 3: 
# 
#  
# 输入: s = "abc"
# 输出: false 
# 
#  
# 
#  提示: 
# 
#  
#  1 <= s.length <= 10⁵ 
#  s 由小写英文字母组成 
#  
#  Related Topics 贪心 双指针 字符串 👍 516 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def validPalindrome(self, s: str) -> bool:
        def helper(ss):
            i=0
            j = len(ss)-1
            while i<j:
                if ss[i]!=ss[j]:
                    return False
                else:
                    i+=1
                    j-=1
            return True

        i=0
        j=len(s)-1
        while i<j:
            if s[i]!=s[j]:
                return helper(s[(i+1):(j+1)]) or helper(s[i:j])
            else:
                i+=1
                j-=1
        return True

# leetcode submit region end(Prohibit modification and deletion)
