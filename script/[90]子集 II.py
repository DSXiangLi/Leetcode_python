# 给你一个整数数组 nums ，其中可能包含重复元素，请你返回该数组所有可能的子集（幂集）。 
# 
#  解集 不能 包含重复的子集。返回的解集中，子集可以按 任意顺序 排列。 
# 
#  
#  
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,2,2]
# 输出：[[],[1],[1,2],[1,2,2],[2],[2,2]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0]
# 输出：[[],[0]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10 
#  -10 <= nums[i] <= 10 
#  
#  
#  
#  Related Topics 位运算 数组 回溯 👍 875 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        result = []

        def backtrace(nums, tmp):
            nonlocal result
            result.append(tmp)
            if not nums:
                return
            for i,n in enumerate(nums):
                if i>0 and nums[i-1]==n:
                    continue
                backtrace(nums[(i+1):], tmp+[n])
        backtrace(sorted(nums), [])
        return result
# leetcode submit region end(Prohibit modification and deletion)
