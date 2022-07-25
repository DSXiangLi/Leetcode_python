# 给你一个由 无重复 正整数组成的集合 nums ，请你找出并返回其中最大的整除子集 answer ，子集中每一元素对 (answer[i], answer[
# j]) 都应当满足：
#  
#  answer[i] % answer[j] == 0 ，或 
#  answer[j] % answer[i] == 0 
#  
# 
#  如果存在多个有效解子集，返回其中任何一个均可。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,3]
# 输出：[1,2]
# 解释：[1,3] 也会被视为正确答案。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1,2,4,8]
# 输出：[1,2,4,8]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 1000 
#  1 <= nums[i] <= 2 * 109 
#  nums 中的所有整数 互不相同 
#  
#  Related Topics 数组 数学 动态规划 排序 
#  👍 459 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestDivisibleSubset(self, nums: List[int]) -> List[int]:
        l = len(nums)
        dp = [1] * l
        nums = sorted(nums)
        maxl = 1
        maxval = nums[0]

        for i in range(l):
            for j in range(i):
                if nums[i]%nums[j]==0:
                    dp[i] = max(dp[i], dp[j]+1)
            if dp[i]>maxl:
                maxl = dp[i]
                maxval = nums[i]
        #反向遍历得到子集
        result = []
        for i in range(l-1,-1,-1):
            if dp[i]==maxl and maxval%nums[i]==0:
                result.append(nums[i])
                maxl-=1
                maxval = nums[i]

        return result

# leetcode submit region end(Prohibit modification and deletion)
