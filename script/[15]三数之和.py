# 给你一个包含 n 个整数的数组 nums，判断 nums 中是否存在三个元素 a，b，c ，使得 a + b + c = 0 ？请你找出所有和为 0 且不重
# 复的三元组。 
# 
#  注意：答案中不可以包含重复的三元组。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-1,0,1,2,-1,-4]
# 输出：[[-1,-1,2],[-1,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = []
# 输出：[]
#  
# 
#  示例 3： 
# 
#  
# 输入：nums = [0]
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  0 <= nums.length <= 3000 
#  -10⁵ <= nums[i] <= 10⁵ 
#  
#  Related Topics 数组 双指针 排序 👍 4982 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        if len(nums)<3:
            return []
        nums = sorted(nums)
        result = []
        for i in range(len(nums)-2):
            a = nums[i]
            left = i+1
            right = len(nums)-1
            if a>0:
                continue
            if i>0 and nums[i]==nums[i-1]:
                continue
            while left<right:
                b = nums[left]
                c = nums[right]
                if left != i+1 and nums[left]==nums[left-1]:
                    left +=1
                    continue
                if right != len(nums)-1 and nums[right]==nums[right+1]:
                    right-=1
                    continue
                if a+b+c==0:
                    result.append([a,b,c])
                    right-=1
                    left +=1
                elif a+b+c>0:
                    right-=1
                else:
                    left+=1
        return result


# leetcode submit region end(Prohibit modification and deletion)
