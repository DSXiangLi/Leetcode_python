# 给定一个整数数组 prices，其中第 prices[i] 表示第 i 天的股票价格 。 
# 
#  设计一个算法计算出最大利润。在满足以下约束条件下，你可以尽可能地完成更多的交易（多次买卖一支股票）: 
# 
#  
#  卖出股票后，你无法在第二天买入股票 (即冷冻期为 1 天)。 
#  
# 
#  注意：你不能同时参与多笔交易（你必须在再次购买前出售掉之前的股票）。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: prices = [1,2,3,0,2]
# 输出: 3 
# 解释: 对应的交易状态为: [买入, 卖出, 冷冻期, 买入, 卖出] 
# 
#  示例 2:

# 
#  
# 输入: prices = [1]
# 输出: 0
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= prices.length <= 5000 
#  0 <= prices[i] <= 1000 
#  
#  Related Topics 数组 动态规划 
#  👍 1272 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        #状态买入，T卖出，T-1卖出，T-2卖出
        l = len(prices)
        b = [0] * l
        s1 = [0] * l # 当天卖出
        s2 = [0] * l # T-1卖出
        s3 = [0] * l # T-2之前卖出
        b[0] = -prices[0]
        for i in range(1, l):
            b[i] = max(b[i-1], s3[i-1]-prices[i], s2[i-1]-prices[i])
            s1[i] = b[i-1]+prices[i]
            s2[i] = s1[i-1]
            s3[i] = max(s3[i-1], s2[i-1])
        return max(s1[-1],s2[-1],s3[-1])


# leetcode submit region end(Prohibit modification and deletion)
