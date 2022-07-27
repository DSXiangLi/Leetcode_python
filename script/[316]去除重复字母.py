# 给你一个字符串 s ，请你去除字符串中重复的字母，使得每个字母只出现一次。需保证 返回结果的字典序最小（要求不能打乱其他字符的相对位置）。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "bcabc"
# 输出："abc"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "cbacdcbc"
# 输出："acdb" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 104 
#  s 由小写英文字母组成 
#  
# 
#  
# 
#  注意：该题与 1081 https://leetcode-cn.com/problems/smallest-subsequence-of-distinct
# -characters 相同 
#  Related Topics 栈 贪心 字符串 单调栈 
#  👍 775 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeDuplicateLetters(self, s: str) -> str:
        from collections import Counter
        hash = Counter(s)
        stack = []
        seen = set()
        # seen 判断是否入栈，hash判断是否出栈
        for i in s:
            if i not in seen:
                while stack and hash[stack[-1]]>0 and i<stack[-1]:
                    seen.discard(stack.pop())
                stack.append(i)
                seen.add(i)
            hash[i]-=1
        return ''.join(stack)

# leetcode submit region end(Prohibit modification and deletion)
