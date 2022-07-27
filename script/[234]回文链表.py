# 给你一个单链表的头节点 head ，请你判断该链表是否为回文链表。如果是，返回 true ；否则，返回 false 。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [1,2,2,1]
# 输出：true
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [1,2]
# 输出：false
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点数目在范围[1, 105] 内 
#  0 <= Node.val <= 9 
#  
# 
#  
# 
#  进阶：你能否用 O(n) 时间复杂度和 O(1) 空间复杂度解决此题？ 
#  Related Topics 栈 递归 链表 双指针 
#  👍 1451 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        def reverse(head):
            newnode = None
            while head:
                nextnode = head.next
                head.next=newnode
                newnode = head
                head = nextnode
            return newnode

        def getmid(head):
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        ptr1 = head
        ptr2 = getmid(head)
        ptr2 = reverse(ptr2)
        while ptr1 and ptr2:
            if ptr1.val !=ptr2.val:
                return False
            ptr1 = ptr1.next
            ptr2 = ptr2.next
        return True

# leetcode submit region end(Prohibit modification and deletion)
