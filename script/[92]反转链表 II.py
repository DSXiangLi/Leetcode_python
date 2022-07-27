# 给你单链表的头指针 head 和两个整数 left 和 right ，其中 left <= right 。请你反转从位置 left 到位置 right 的链
# 表节点，返回 反转后的链表 。
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,3,4,5], left = 2, right = 4
# 输出：[1,4,3,2,5]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [5], left = 1, right = 1
# 输出：[5]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目为 n 
#  1 <= n <= 500 
#  -500 <= Node.val <= 500 
#  1 <= left <= right <= n 
#  
# 
#  
# 
#  进阶： 你可以使用一趟扫描完成反转吗？ 
#  Related Topics 链表 
#  👍 1356 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: ListNode, left: int, right: int) -> ListNode:
        dummy = ListNode()
        dummy.next = head

        ptrl,ptrr = dummy,dummy
        for i in range(left-1):
            ptrl = ptrl.next
        for i in range(right):
            ptrr = ptrr.next

        left = ptrl.next
        # 断开右边
        right = ptrr
        right_next = right.next
        right.next = None

        def reverse(head):
            newnode = None
            cur = head
            while cur:
                nextnode = cur.next
                cur.next=newnode
                newnode = cur
                cur = nextnode
            return newnode

        mid = reverse(left) #翻转
        ptrl.next = mid #左边接入
        left.next = right_next  # 右边接入
        return dummy.next
# leetcode submit region end(Prohibit modification and deletion)
