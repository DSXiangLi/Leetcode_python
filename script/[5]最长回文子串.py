# 给你一个字符串 s，找到 s 中最长的回文子串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "babad"
# 输出："bab"
# 解释："aba" 同样是符合题意的答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbbd"
# 输出："bb"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 1000 
#  s 仅由数字和英文字母组成 
#  
#  Related Topics 字符串 动态规划 👍 5464 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestPalindrome(self, s: str) -> str:
        if len(s)<=1:
            return s
        def get_boundary(pos1, pos2):
            while  pos1>=0 and pos2<len(s) and s[pos1]==s[pos2]:
                pos1-=1
                pos2+=1
            return pos1, pos2
        start,end = 0,0

        for i in range(1, len(s)):
            left1, right1 = get_boundary(i-1, i)
            left2, right2 = get_boundary(i-1, i+1)

            if right1-left1 > end-start:
                start,end = left1, right1
            if right2 - left2>end-start:
                start, end = left2, right2
        return s[(start+1):end]



# leetcode submit region end(Prohibit modification and deletion)
