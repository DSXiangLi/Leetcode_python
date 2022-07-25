# 给定一个字符串 s 和一个字符串 t ，计算在 s 的子序列中 t 出现的个数。 
# 
#  字符串的一个 子序列 是指，通过删除一些（也可以不删除）字符且不干扰剩余字符相对位置所组成的新字符串。（例如，"ACE" 是 "ABCDE" 的一个子序列
# ，而 "AEC" 不是） 
# 
#  题目数据保证答案符合 32 位带符号整数范围。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "rabbbit", t = "rabbit"
# 输出：3
# 解释：
# 如下图所示, 有 3 种可以从 s 中得到 "rabbit" 的方案。
# rabbbit
# rabbbit
# rabbbit 
# 
#  示例 2： 
# 
#  
# 输入：s = "babgbag", t = "bag"
# 输出：5
# 解释：
# 如下图所示, 有 5 种可以从 s 中得到 "bag" 的方案。 
# babgbag
# babgbag
# babgbag
# babgbag
# babgbag
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s.length, t.length <= 1000 
#  s 和 t 由英文字母组成 
#  
#  Related Topics 字符串 动态规划 
#  👍 823 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def numDistinct(self, s: str, t: str) -> int:
        ls = len(s)
        lt = len(t)
        dp = [[1] + [0] * lt for i in range(ls+1)] # t=''的时候出现1次
        # dp[i][j]是前i个s里面有几个前j个t字符= 前i-1个s有多少个j-1个t+ 前i-个s有多少个j个t
        for i in range(1, ls+1):
            for j in range(1, lt+1):
                if s[i-1]==t[j-1]:
                    dp[i][j] = dp[i-1][j-1] + dp[i-1][j]
                else:
                    dp[i][j] = dp[i-1][j]
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
