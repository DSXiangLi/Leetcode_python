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



Tips

大根堆问题，因为python只有小根堆的数据结构，所以需要number取负数，保留K个最大的负数->k个最小的正数