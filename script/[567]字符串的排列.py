# 给你两个字符串 s1 和 s2 ，写一个函数来判断 s2 是否包含 s1 的排列。如果是，返回 true ；否则，返回 false 。 
# 
#  换句话说，s1 的排列之一是 s2 的 子串 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：s1 = "ab" s2 = "eidbaooo"
# 输出：true
# 解释：s2 包含 s1 的排列之一 ("ba").
#  
# 
#  示例 2： 
# 
#  
# 输入：s1= "ab" s2 = "eidboaoo"
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= s1.length, s2.length <= 10⁴ 
#  s1 和 s2 仅包含小写字母 
#  
#  Related Topics 哈希表 双指针 字符串 滑动窗口 👍 723 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s2)<len(s1):
            return False
        hash1 = [0] * 26
        hash2 = [0] * 26
        l1 = len(s1)
        for i in s1:
            hash1[ord(i)-ord('a')]+=1
        for i in s2[:l1]:
            hash2[ord(i) - ord('a')] += 1
        if hash1==hash2:
            return True

        for i in range(l1, len(s2)):
            hash2[ord(s2[i])-ord('a')]+=1
            hash2[ord(s2[i-l1])-ord('a')]-=1
            if hash1==hash2:
                return True
        return False
# leetcode submit region end(Prohibit modification and deletion)

