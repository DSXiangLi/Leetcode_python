# 给你一个由 n 个整数组成的数组 nums ，和一个目标值 target 。请你找出并返回满足下述全部条件且不重复的四元组 [nums[a], nums[
# b], nums[c], nums[d]] （若两个四元组元素一一对应，则认为两个四元组重复）： 
# 
#  
#  0 <= a, b, c, d < n 
#  a、b、c 和 d 互不相同 
#  nums[a] + nums[b] + nums[c] + nums[d] == target 
#  
# 
#  你可以按 任意顺序 返回答案 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,0,-1,0,-2,2], target = 0
# 输出：[[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [2,2,2,2,2], target = 8
# 输出：[[2,2,2,2]]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 200 
#  -10⁹ <= nums[i] <= 10⁹ 
#  -10⁹ <= target <= 10⁹ 
#  
#  Related Topics 数组 双指针 排序 👍 1297 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        nums = sorted(nums)
        if len(nums)<4:
            return []
        l = len(nums)
        result = []
        for i in range(l-3):
            if i!=0 and nums[i]==nums[i-1]:
                continue
            for j in range(i+1, l-2):
                if j!=i+1 and nums[j]==nums[j-1]:
                    continue
                left = j+1
                right = l-1
                res= nums[i] + nums[j]
                while left<right:
                    total = res+nums[left]+nums[right]
                    if left != j+1 and nums[left]==nums[left-1]:
                        left+=1
                        continue
                    if right != l-1 and nums[right]==nums[right+1]:
                        right-=1
                        continue
                    if total==target:
                        result.append([nums[i],nums[j],nums[left], nums[right]])
                        left+=1
                        right-=1
                    elif total<target:
                        left+=1
                    else:
                        right-=1
        return result
# leetcode submit region end(Prohibit modification and deletion)
