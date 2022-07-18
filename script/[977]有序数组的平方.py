# 给你一个按 非递减顺序 排序的整数数组 nums，返回 每个数字的平方 组成的新数组，要求也按 非递减顺序 排序。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [-4,-1,0,3,10]
# 输出：[0,1,9,16,100]
# 解释：平方后，数组变为 [16,1,0,9,100]
# 排序后，数组变为 [0,1,9,16,100] 
# 
#  示例 2： 
# 
#  
# 输入：nums = [-7,-3,2,3,11]
# 输出：[4,9,9,49,121]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁴ 
#  -10⁴ <= nums[i] <= 10⁴ 
#  nums 已按 非递减顺序 排序 
#  
# 
#  
# 
#  进阶： 
# 
#  
#  请你设计时间复杂度为 O(n) 的算法解决本问题 
#  
#  Related Topics 数组 双指针 排序 👍 578 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        neg_pos = -1

        for i,n in enumerate(nums):
            if n<0:
                neg_pos = i
            else:
                break
        pos_pos = neg_pos+1
        l = len(nums)
        result =[]
        while neg_pos>=0 and pos_pos < l:
            if nums[neg_pos]**2<nums[pos_pos]**2:
                result.append(nums[neg_pos]**2)
                neg_pos-=1
            else:
                result.append(nums[pos_pos]**2)
                pos_pos+=1

        while neg_pos>=0:
            result.append(nums[neg_pos]**2)
            neg_pos -= 1
        while pos_pos<l:
            result.append(nums[pos_pos] ** 2)
            pos_pos += 1
        return result

# leetcode submit region end(Prohibit modification and deletion)
