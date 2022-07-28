# 给定一组非负整数 nums，重新排列每个数的顺序（每个数不可拆分）使之组成一个最大的整数。 
# 
#  注意：输出结果可能非常大，所以你需要返回一个字符串而不是整数。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [10,2]
# 输出："210" 
# 
#  示例 2： 
# 
#  
# 输入：nums = [3,30,34,5,9]
# 输出："9534330"
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 100 
#  0 <= nums[i] <= 109 
#  
#  Related Topics 贪心 字符串 排序 
#  👍 978 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        def cmp(a,b):
            if a+b<b+a:
                return -1
            elif a+b==b+a:
                return 0
            else:
                return 1
        nums = sorted([str(i) for i in nums], key=functools.cmp_to_key(cmp), reverse=True)
        if nums[0]=='0':
            return '0'
        else:
            return ''.join(nums)
# leetcode submit region end(Prohibit modification and deletion)
