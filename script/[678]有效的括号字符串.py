# 给定一个只包含三种字符的字符串：（ ，） 和 *，写一个函数来检验这个字符串是否为有效字符串。有效字符串具有如下规则： 
# 
#  
#  任何左括号 ( 必须有相应的右括号 )。 
#  任何右括号 ) 必须有相应的左括号 ( 。 
#  左括号 ( 必须在对应的右括号之前 )。 
#  * 可以被视为单个右括号 ) ，或单个左括号 ( ，或一个空字符串。 
#  一个空字符串也被视为有效字符串。 
#  
# 
#  示例 1: 
# 
#  
# 输入: "()"
# 输出: True
#  
# 
#  示例 2: 
# 
#  
# 输入: "(*)"
# 输出: True
#  
# 
#  示例 3: 
# 
#  
# 输入: "(*))"
# 输出: True
#  
# 
#  注意: 
# 
#  
#  字符串大小将在 [1，100] 范围内。 
#  
#  Related Topics 栈 贪心 字符串 动态规划 
#  👍 508 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def checkValidString(self, s: str) -> bool:
        # 从左到右
        cnt =0
        for i in s:
            if i=='(':
                cnt+=1
            elif i==')':
                cnt-=1
            else:
                cnt+=1
            if cnt<0:
                return False
        cnt = 0
        for i in s[::-1]:
            if i==')':
                cnt+=1
            elif i=='(':
                cnt-=1
            else:
                cnt+=1
            if cnt<0:
                return False
        return True
# leetcode submit region end(Prohibit modification and deletion)
