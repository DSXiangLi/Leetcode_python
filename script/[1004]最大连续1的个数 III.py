# 给定一个二进制数组 nums 和一个整数 k，如果可以翻转最多 k 个 0 ，则返回 数组中连续 1 的最大个数 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,1,1,0,0,0,1,1,1,1,0], K = 2
# 输出：6
# 解释：[1,1,1,0,0,1,1,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 6。 
# 
#  示例 2： 
# 
#  
# 输入：nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], K = 3
# 输出：10
# 解释：[0,0,1,1,1,1,1,1,1,1,1,1,0,0,0,1,1,1,1]
# 粗体数字从 0 翻转到 1，最长的子数组长度为 10。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 10⁵ 
#  nums[i] 不是 0 就是 1 
#  0 <= k <= nums.length 
#  
#  Related Topics 数组 二分查找 前缀和 滑动窗口 👍 441 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        counter = 0
        maxl = 0
        left = 0
        for i,n in enumerate(nums):
            if n==0:
                counter+=1
            while counter>k and left<=i:
                if nums[left]==0:
                    counter-=1
                left+=1
            maxl = max(maxl, i-left+1)
        return maxl
# leetcode submit region end(Prohibit modification and deletion)
