# 给定整数数组 nums 和整数 k，请返回数组中第 k 个最大的元素。 
# 
#  请注意，你需要找的是数组排序后的第 k 个最大的元素，而不是第 k 个不同的元素。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: [3,2,1,5,6,4], k = 2
# 输出: 5
#  
# 
#  示例 2: 
# 
#  
# 输入: [3,2,3,1,2,4,5,5,6], k = 4
# 输出: 4 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= k <= nums.length <= 105 
#  -104 <= nums[i] <= 104 
#  
#  Related Topics 数组 分治 快速选择 排序 堆（优先队列） 
#  👍 1787 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        def partition(nums, left, right):
            key = left
            while left<right:
                while left<right and nums[key]<=nums[right]:
                    right-=1
                while left<right and nums[left]<=nums[key]:
                    left+=1
                nums[left], nums[right] = nums[right],nums[left]
            nums[left], nums[key] = nums[key], nums[left]
            return left

        def sort(nums, left, right):
            if left>=right:
                return
            mid = partition(nums, left, right)
            if mid==k:
                return
            elif mid<k:
                sort(nums, mid + 1, right)
            else:
                sort(nums, left, mid-1)

        l = len(nums)
        k = l-k
        sort(nums, 0, len(nums)-1)
        return nums[k]
# leetcode submit region end(Prohibit modification and deletion)
