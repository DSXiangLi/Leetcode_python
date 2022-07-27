# 给你一个链表的头节点 head 和一个特定值 x ，请你对链表进行分隔，使得所有 小于 x 的节点都出现在 大于或等于 x 的节点之前。 
# 
#  你应当 保留 两个分区中每个节点的初始相对位置。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,4,3,2,5,2], x = 3
# 输出：[1,2,2,4,3,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [2,1], x = 2
# 输出：[1,2]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 200] 内 
#  -100 <= Node.val <= 100 
#  -200 <= x <= 200 
#  
#  Related Topics 链表 双指针 
#  👍 595 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        small = ListNode()
        big = ListNode()
        ptr_small = small
        ptr_big = big
        while head:
            if head.val >= x:
                ptr_big.next= head
                ptr_big = ptr_big.next
            else:
                ptr_small.next=head
                ptr_small = ptr_small.next
            head = head.next
        ptr_small.next= big.next
        ptr_big.next =None
        return small.next
# leetcode submit region end(Prohibit modification and deletion)
