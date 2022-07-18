# 给你一个整数数组 nums ，找出并返回所有该数组中不同的递增子序列，递增子序列中 至少有两个元素 。你可以按 任意顺序 返回答案。 
# 
#  数组中可能含有重复元素，如出现两个整数相等，也可以视作递增序列的一种特殊情况。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [4,6,7,7]
# 输出：[[4,6],[4,6,7],[4,6,7,7],[4,7],[4,7,7],[6,7],[6,7,7],[7,7]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [4,4,3,2,1]
# 输出：[[4,4]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 15 
#  -100 <= nums[i] <= 100 
#  
#  Related Topics 位运算 数组 哈希表 回溯 👍 474 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        result = []
        def backtrace(nums, tmp):
            nonlocal result
            if len(tmp)>=2:
                result.append(tmp)
            if not nums:
                return
            visited = set()

            for i,n in enumerate(nums):
                if n in visited:
                    continue
                if not tmp or n>=tmp[-1]:
                    backtrace(nums[(i+1):], tmp+[n])
                    visited.add(n)
        backtrace(nums,[])
        return result


# leetcode submit region end(Prohibit modification and deletion)
