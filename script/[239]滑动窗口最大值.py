# 给你一个整数数组 nums，有一个大小为 k 的滑动窗口从数组的最左侧移动到数组的最右侧。你只可以看到在滑动窗口内的 k 个数字。滑动窗口每次只向右移动一位
# 。 
# 
#  返回 滑动窗口中的最大值 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums = [1,3,-1,-3,5,3,6,7], k = 3
# 输出：[3,3,5,5,6,7]
# 解释：
# 滑动窗口的位置                最大值
# ---------------               -----
# [1  3  -1] -3  5  3  6  7       3
#  1 [3  -1  -3] 5  3  6  7       3
#  1  3 [-1  -3  5] 3  6  7       5
#  1  3  -1 [-3  5  3] 6  7       5
#  1  3  -1  -3 [5  3  6] 7       6
#  1  3  -1  -3  5 [3  6  7]      7
#  
# 
#  示例 2： 
# 
#  
# 输入：nums = [1], k = 1
# 输出：[1]
#  
# 
#  
# 
#  提示： 
# 
#  
#  1 <= nums.length <= 105 
#  -104 <= nums[i] <= 104 
#  1 <= k <= nums.length 
#  
#  Related Topics 队列 数组 滑动窗口 单调队列 堆（优先队列） 
#  👍 1759 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        from collections import deque
        que = deque([nums[0]])
        # 维护一个k个元素内部的单调减的队列
        for i in range(1, k):
            while que and nums[i]>que[-1]:
                que.pop()
            que.append(nums[i])
        result = []
        for i in range(k, len(nums)):
            result.append(que[0])
            if nums[i-k]==que[0]:
                que.popleft()
            while que and nums[i]>que[-1]:
                que.pop()
            que.append(nums[i])
        result.append(que[0])

        return result


# leetcode submit region end(Prohibit modification and deletion)
