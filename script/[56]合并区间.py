# 以数组 intervals 表示若干个区间的集合，其中单个区间为 intervals[i] = [starti, endi] 。请你合并所有重叠的区间，并返
# 回 一个不重叠的区间数组，该数组需恰好覆盖输入中的所有区间 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：intervals = [[1,3],[2,6],[8,10],[15,18]]
# 输出：[[1,6],[8,10],[15,18]]
# 解释：区间 [1,3] 和 [2,6] 重叠, 将它们合并为 [1,6].
#  
# 
#  示例 2： 
# 
#  
# 输入：intervals = [[1,4],[4,5]]
# 输出：[[1,5]]
# 解释：区间 [1,4] 和 [4,5] 可被视为重叠区间。 
# 
#  
# 
#  提示： 
# 
#  
#  1 <= intervals.length <= 104 
#  intervals[i].length == 2 
#  0 <= starti <= endi <= 104 
#  
#  Related Topics 数组 排序 
#  👍 1572 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        result = []
        intervals = sorted(intervals, key=lambda x:x[0])
        tmp = intervals[0]
        for i in range(1, len(intervals)):
            if intervals[i][0] <= tmp[1]:
                tmp[1] = max(intervals[i][1],tmp[1])
            else:
                result.append(tmp)
                tmp = intervals[i]
        result.append(tmp)
        return result
# leetcode submit region end(Prohibit modification and deletion)
