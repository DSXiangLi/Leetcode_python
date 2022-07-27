# 给你链表的头结点 head ，请将其按 升序 排列并返回 排序后的链表 。 
# 
#  
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：head = [4,2,1,3]
# 输出：[1,2,3,4]
#  
# 
#  示例 2： 
# 
#  
# 输入：head = [-1,5,3,4,0]
# 输出：[-1,0,3,4,5]
#  
# 
#  示例 3： 
# 
#  
# 输入：head = []
# 输出：[]
#  
# 
#  
# 
#  提示： 
# 
#  
#  链表中节点的数目在范围 [0, 5 * 104] 内 
#  -105 <= Node.val <= 105 
#  
# 
#  
# 
#  进阶：你可以在 O(n log n) 时间复杂度和常数级空间复杂度下，对链表进行排序吗？ 
#  Related Topics 链表 双指针 分治 排序 归并排序 
#  👍 1718 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def merge(l1, l2):
            newnode = ListNode(-1)
            ptr = newnode
            while l1 and l2:
                if l1.val < l2.val:
                    ptr.next =l1
                    l1 = l1.next
                else:
                    ptr.next=l2
                    l2 = l2.next
                ptr = ptr.next
            if l1:
                ptr.next=l1
            if l2:
                ptr.next=l2
            return newnode.next

        def getmid(head):
            slow, fast = head, head
            while fast.next and fast.next.next:
                slow = slow.next
                fast = fast.next.next
            return slow

        def sort_merge(head):
            if not head or not head.next:
                return head
            left = getmid(head)
            right = left.next
            left.next=None
            left = sort_merge(head)
            right = sort_merge(right)
            return merge(left, right )
        return sort_merge(head)

# leetcode submit region end(Prohibit modification and deletion)
