输入整数数组 arr ，找出其中最小的 k 个数。例如，输入4、5、1、6、2、7、3、8这8个数字，则最小的4个数字是1、2、3、4。

 

示例 1：

输入：arr = [3,2,1], k = 2
输出：[1,2] 或者 [2,1]

示例 2：

输入：arr = [0,1,2,1], k = 1
输出：[0]

 

限制：

    0 <= k <= arr.length <= 10000
    0 <= arr[i] <= 10000

1. 堆排序

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        if k==0:
            return list()
        nums = [-i for i in arr[:k]]
        heapq.heapify(nums)
        for i in arr[k:]:
            if -i > nums[0]:
                heapq.heappop(nums)
                heapq.heappush(nums, -i)
        return [-x for x in nums]
```



2. 快速排序

```python
class Solution:
    def getLeastNumbers(self, arr: List[int], k: int) -> List[int]:
        def partition(nums, left, right):
            key = left
            while left<right:
                while left<right and nums[right]>=nums[key]:
                    right-=1
                while left<right and nums[left]<=nums[key]:
                    left+=1
                nums[left], nums[right] = nums[right],nums[left]
            nums[left],nums[key] =nums[key],nums[left]
            return left

        def quick_sort(nums, left, right):
            if left>=right:
                return
            
            mid = partition(nums, left, right)
            if k<mid:
                quick_sort(nums, left, mid - 1)
            else:
                quick_sort(arr, mid + 1, right)

        l = len(arr)
        if k>l:
            return arr
        quick_sort(arr, 0, l-1)
        return arr[:k]
```



快速排序解法

1. 注意partition过程中，保证右边是>=key， 左边是<=key，且左右是不对称的需要先遍历右边
2. 在sort过程中，可以通过和k判断位置只对一半的位置进行排序
3. 注意sort过程的停止条件，默认是left>=right，如果找k大的停止条件还有mid==k

