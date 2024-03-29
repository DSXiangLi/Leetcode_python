# 给你一个只包含 '(' 和 ')' 的字符串，找出最长有效（格式正确且连续）括号子串的长度。 
# 
#  
# 
#  
#  
#  示例 1： 
# 
#  
# 输入：s = "(()"
# 输出：2
# 解释：最长有效括号子串是 "()"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = ")()())"
# 输出：4
# 解释：最长有效括号子串是 "()()"
#  
# 
#  示例 3： 
# 
#  
# 输入：s = ""
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length <= 3 * 104 
#  s[i] 为 '(' 或 ')' 
#  
#  
#  
#  Related Topics 栈 字符串 动态规划 
#  👍 1922 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestValidParentheses(self, s: str) -> int:
        maxl = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i]=='(':
                stack.append(i)
            else:
                stack.pop() #
                if not stack:
                    stack.append(i) # 右括号隔断情况
                else:
                    maxl = max(maxl, i-stack[-1])
        return maxl
# leetcode submit region end(Prohibit modification and deletion)
