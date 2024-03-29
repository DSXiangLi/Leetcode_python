# 给定一个二进制数组 nums ， 计算其中最大连续 1 的个数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,0,1,1,1]
# 输出：3
# 解释：开头的两位和最后的三位都是连续 1 ，所以最大连续 1 的个数是 3.
#  
# 
#  示例 2: 
# 
#  
# 输入：nums = [1,0,1,1,0,1]
# 输出：2
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  nums[i] 不是 0 就是 1. 
#  
#  Related Topics 数组 
#  👍 327 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        counter = 0
        maxcount =0
        for i,n in enumerate(nums):
            if n==1:
                counter+=1
            else:
                maxcount = max(maxcount, counter)
                counter =0
        maxcount = max(maxcount, counter)
        return maxcount
# leetcode submit region end(Prohibit modification and deletion)
