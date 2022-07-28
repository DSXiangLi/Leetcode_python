# 给定三个字符串 s1、s2、s3，请你帮忙验证 s3 是否是由 s1 和 s2 交错 组成的。 
# 
#  两个字符串 s 和 t 交错 的定义与过程如下，其中每个字符串都会被分割成若干 非空 子字符串： 
# 
#  
#  s = s1 + s2 + ... + sn 
#  t = t1 + t2 + ... + tm 
#  |n - m| <= 1 
#  交错 是 s1 + t1 + s2 + t2 + s3 + t3 + ... 或者 t1 + s1 + t2 + s2 + t3 + s3 + ... 
#  
# 
#  注意：a + b 意味着字符串 a 和 b 连接。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
# 输出：false
#  
# 
#  示例 3： 
# 
#  
# 输入：s1 = "", s2 = "", s3 = ""
# 输出：true
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= s1.length, s2.length <= 100 
#  0 <= s3.length <= 200 
#  s1、s2、和 s3 都由小写英文字母组成 
#  
# 
#  
# 
#  进阶：您能否仅使用 O(s2.length) 额外的内存空间来解决它? 
#  Related Topics 字符串 动态规划 
#  👍 737 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1 = len(s1)
        l2 = len(s2)
        l3 = len(s3)
        if l1+l2!=l3:
            return False
        dp = [[False] * (l2+1) for i in range(1+l1)]
        dp[0][0]=True
        for i in range(1, l1+1):
            dp[i][0] = dp[i-1][0] and s1[i-1]==s3[i-1]
        for i in range(1, l2+1):
            dp[0][i] = dp[0][i-1] and s2[i-1]==s3[i-1]
        print(dp)
        for i in range(1, l1+1):
            for j in range(1,l2+1):
                pos = i+j-1
                dp[i][j] = (dp[i-1][j] and s1[i-1]==s3[pos]) or (dp[i][j-1] and s2[j-1]==s3[pos])
        return dp[-1][-1]
# leetcode submit region end(Prohibit modification and deletion)
