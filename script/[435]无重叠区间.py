# 给定一个区间的集合 intervals ，其中 intervals[i] = [starti, endi] 。返回 需要移除区间的最小数量，使剩余区间互不重
# 叠 。 
# 
#  
# 
#  示例 1: 
# 
#  
# 输入: intervals = [[1,2],[2,3],[3,4],[1,3]]
# 输出: 1
# 解释: 移除 [1,3] 后，剩下的区间没有重叠。
#  
# 
#  示例 2: 
# 
#  
# 输入: intervals = [ [1,2], [1,2], [1,2] ]
# 输出: 2
# 解释: 你需要移除两个 [1,2] 来使剩下的区间没有重叠。
#  
# 
#  示例 3: 
# 
#  
# 输入: intervals = [ [1,2], [2,3] ]
# 输出: 0
# 解释: 你不需要移除任何区间，因为它们已经是无重叠的了。
#  
# 
#  
# 
#  提示: 
# 
#  
#  1 <= intervals.length <= 105 
#  intervals[i].length == 2 
#  -5 * 104 <= starti < endi <= 5 * 104 
#  
#  Related Topics 贪心 数组 动态规划 排序 
#  👍 751 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        intervals = sorted(intervals, key = lambda x:x[1])
        right = intervals[0][1]
        tmp = intervals[0]
        counter = 0
        for i in range(1, len(intervals)):
            if intervals[i][0]<right:
                counter+=1
            else:
                right = intervals[i][1]
        return counter


# leetcode submit region end(Prohibit modification and deletion)
