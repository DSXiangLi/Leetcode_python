# 实现 strStr() 函数。 
# 
#  给你两个字符串 haystack 和 needle ，请你在 haystack 字符串中找出 needle 字符串出现的第一个位置（下标从 0 开始）。如
# 果不存在，则返回 -1 。 
# 
#  说明： 
# 
#  当 needle 是空字符串时，我们应当返回什么值呢？这是一个在面试中很好的问题。 
# 
#  对于本题而言，当 needle 是空字符串时我们应当返回 0 。这与 C 语言的 strstr() 以及 Java 的 indexOf() 定义相符。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：haystack = "hello", needle = "ll"
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：haystack = "aaaaa", needle = "bba"
# 输出：-1
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= haystack.length, needle.length <= 104 
#  haystack 和 needle 仅由小写英文字符组成 
#  
#  Related Topics 双指针 字符串 字符串匹配 
#  👍 1520 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        def getnext(needle):
            l = len(needle)
            ptr1 = 0
            ptr2 = -1
            next = [-1] * l #相同前缀长度
            while ptr1<(l-1):
                if ptr2==-1 or needle[ptr1] ==needle[ptr2]:
                    # 每一步更新的是下一个字符的前缀长度
                    ptr1+=1 #下一个字符
                    ptr2+=1 # 从哪一个位置开始匹配
                    next[ptr1] = ptr2
                else:
                    # 上一个字符匹配到的位置重新开始匹配
                    ptr2 = next[ptr2]
            return next
        next = getnext(needle)
        l1 = len(haystack)
        l2 = len(needle)
        ptr1 =0
        ptr2 =0
        while ptr1<l1 and ptr2 <l2:
            if ptr2==-1 or haystack[ptr1] == needle[ptr2]:
                ptr1+=1
                ptr2+=1
            else:
                ptr2 = next[ptr2]
        if ptr2==l2:
            return ptr1-ptr2
        else:
            return -1

# leetcode submit region end(Prohibit modification and deletion)


