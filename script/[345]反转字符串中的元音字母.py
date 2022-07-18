# 给你一个字符串 s ，仅反转字符串中的所有元音字母，并返回结果字符串。 
# 
#  元音字母包括 'a'、'e'、'i'、'o'、'u'，且可能以大小写两种形式出现。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s = "hello"
# 输出："holle"
#  
# 
#  示例 2： 
# 
#  
# 输入：s = "leetcode"
# 输出："leotcede" 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s.length <= 3 * 10⁵ 
#  s 由 可打印的 ASCII 字符组成 
#  
#  Related Topics 双指针 字符串 👍 255 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def reverseVowels(self, s: str) -> str:
        left =0
        right =len(s)-1
        alpha = {'a','e','i','o','u'}
        s = list(s)
        while left<right:
            if s[left].lower() not in alpha:
                left +=1
                continue
            if s[right].lower() not in alpha:
                right -=1
                continue
            if s[left].lower() in alpha and s[right].lower() in alpha:
                s[left], s[right] = s[right], s[left]
            left +=1
            right-=1
        return ''.join(s)

# leetcode submit region end(Prohibit modification and deletion)
