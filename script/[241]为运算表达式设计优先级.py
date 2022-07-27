# 给你一个由数字和运算符组成的字符串 expression ，按不同优先级组合数字和运算符，计算并返回所有可能组合的结果。你可以 按任意顺序 返回答案。 
# 
#  生成的测试用例满足其对应输出值符合 32 位整数范围，不同结果的数量不超过 104 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：expression = "2-1-1"
# 输出：[0,2]
# 解释：
# ((2-1)-1) = 0 
# (2-(1-1)) = 2
#  
# 
#  示例 2： 
# 
#  
# 输入：expression = "2*3-4*5"
# 输出：[-34,-14,-10,-10,10]
# 解释：
# (2*(3-(4*5))) = -34 
# ((2*3)-(4*5)) = -14 
# ((2*(3-4))*5) = -10 
# (2*((3-4)*5)) = -10 
# (((2*3)-4)*5) = 10
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= expression.length <= 20 
#  expression 由数字和算符 '+'、'-' 和 '*' 组成。 
#  输入表达式中的所有整数值在范围 [0, 99] 
#  
#  Related Topics 递归 记忆化搜索 数学 字符串 动态规划 
#  👍 732 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def diffWaysToCompute(self, expression: str) -> List[int]:
        hash = {}
        def dfs(expression):
            if  expression.isdigit():
                return [int(expression)]
            if expression in hash:
                return hash[expression]
            res = []
            for i, n in enumerate(expression):
                if n in ['+','-','*','']:
                    left= dfs(expression[:i])
                    right=dfs(expression[(i+1):])
                    for l in left:
                        for r in right:
                            res.append(eval('{}{}{}'.format(l,n,r)))
            hash[expression] = res
            return res
        return dfs(expression)



# leetcode submit region end(Prohibit modification and deletion)
