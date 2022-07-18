# 给你一个字符串 s，请你将 s 分割成一些子串，使每个子串都是 回文串 。返回 s 所有可能的分割方案。 
# 
#  回文串 是正着读和反着读都一样的字符串。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "aab"
# 输出：[["a","a","b"],["aa","b"]]
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "a"
# 输出：[["a"]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 16 
#  s 仅由小写英文字母组成 
#  
#  Related Topics 字符串 动态规划 回溯 👍 1194 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        result = []

        def is_valid(ss):
            l = len(ss)
            if l==1:
                return True
            for i in range(int(l)//2):
                if ss[i]!= ss[l-i-1]:
                    return False
            return True

        def backtrace(s, tmp):
            nonlocal result
            if not s:
                result.append(tmp)
                return

            for i in range(1, len(s)+1):
                if is_valid(s[:i]):
                    backtrace(s[i:], tmp+[s[:i]])
        backtrace(s, [])
        return result


# leetcode submit region end(Prohibit modification and deletion)
