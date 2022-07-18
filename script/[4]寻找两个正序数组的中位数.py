# 给定两个大小分别为 m 和 n 的正序（从小到大）数组 nums1 和 nums2。请你找出并返回这两个正序数组的 中位数 。 
# 
#  算法的时间复杂度应该为 O(log (m+n)) 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：nums1 = [1,3], nums2 = [2]
# 输出：2.00000
# 解释：合并数组 = [1,2,3] ，中位数 2
#  
# 
#  示例 2： 
# 
#  
# 输入：nums1 = [1,2], nums2 = [3,4]
# 输出：2.50000
# 解释：合并数组 = [1,2,3,4] ，中位数 (2 + 3) / 2 = 2.5
#  
# 
#  
# 
#  
# 
#  提示： 
# 
#  
#  nums1.length == m 
#  nums2.length == n 
#  0 <= m <= 1000 
#  0 <= n <= 1000 
#  1 <= m + n <= 2000 
#  -10⁶ <= nums1[i], nums2[i] <= 10⁶ 
#  
#  Related Topics 数组 二分查找 分治 👍 5626 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        l1 = len(nums1)
        l2 = len(nums2)
        total = l1+l2

        def helper(k):
            index1 =0
            index2 =0
            while True:
                if index1==l1:
                    return nums2[index2+k-1]
                if index2==l2:
                    return nums1[index1+k-1]
                if k==1:
                    return min(nums1[index1], nums2[index2])

                newindex1 = min(index1+ k//2-1, l1-1) #右边界是闭区间 取min避免指针越界
                newindex2 = min(index2+ k//2-1, l2-1)
                if nums1[newindex1] <= nums2[newindex2]:
                    k-=(newindex1-index1+1)
                    index1 = newindex1+1
                else:
                    k-=(newindex2-index2+1)
                    index2 = newindex2 + 1


        if total%2==0:
            return (helper(total//2) + helper(total//2+1))/2
        else:
            return helper(total//2+1)

# leetcode submit region end(Prohibit modification and deletion)
