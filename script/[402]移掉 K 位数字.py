# 给你一个以字符串表示的非负整数 num 和一个整数 k ，移除这个数中的 k 位数字，使得剩下的数字最小。请你以字符串形式返回这个最小的数字。 
#  
# 
#  示例 1 ： 
# 
#  
# 输入：num = "1432219", k = 3
# 输出："1219"
# 解释：移除掉三个数字 4, 3, 和 2 形成一个新的最小的数字 1219 。
#  
# 
#  示例 2 ： 
# 
#  
# 输入：num = "10200", k = 1
# 输出："200"
# 解释：移掉首位的 1 剩下的数字为 200. 注意输出不能有任何前导零。
#  
# 
#  示例 3 ： 
# 
#  
# 输入：num = "10", k = 2
# 输出："0"
# 解释：从原数字移除所有的数字，剩余为空就是 0 。
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= num.length <= 105 
#  num 仅由若干位数字（0 - 9）组成 
#  除了 0 本身之外，num 不含任何前导零 
#  
#  Related Topics 栈 贪心 字符串 单调栈 
#  👍 847 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        stack = []
        for i in num:
            while stack and k>0 and i<stack[-1]:
                k-=1
                stack.pop()
            stack.append(i)

        remain = len(stack)-k
        if remain==0:
            return '0'
        return str(int(''.join(stack[:remain])))
# leetcode submit region end(Prohibit modification and deletion)
