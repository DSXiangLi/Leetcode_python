# 给你一个长度为 n 的整数数组 nums 和 一个目标值 target。请你从 nums 中选出三个整数，使它们的和与 target 最接近。 
# 
#  返回这三个数的和。 
# 
#  假定每组输入只存在恰好一个解。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,2,1,-4], target = 1
# 输出：2
# 解释：与 target 最接近的和是 2 (-1 + 2 + 1 = 2) 。
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,0], target = 1
# 输出：0
#  
# 
#  
# 
#  提示： 
# 
#  
#  3 <= nums.length <= 1000 
#  -1000 <= nums[i] <= 1000 
#  -10⁴ <= target <= 10⁴ 
#  
#  Related Topics 数组 双指针 排序 👍 1195 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums = sorted(nums)
        remainder = float('inf')
        result = None
        for i in range(len(nums)-2):
            a = nums[i]
            left = i+1
            right = len(nums)-1
            while left<right:
                b = nums[left]
                c = nums[right]
                if a+b+c==target:
                    return target
                elif a+b+c>target:
                    right-=1
                else:
                    left+=1
                if abs(target-a-b-c)< remainder:
                    remainder = abs(target-a-b-c)
                    result =a+b+c
        return result

# leetcode submit region end(Prohibit modification and deletion)
