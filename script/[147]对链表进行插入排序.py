# 给定单个链表的头 head ，使用 插入排序 对链表进行排序，并返回 排序后链表的头 。 
# 
#  插入排序 算法的步骤: 
# 
#  
#  插入排序是迭代的，每次只移动一个元素，直到所有元素可以形成一个有序的输出列表。 
#  每次迭代中，插入排序只从输入数据中移除一个待排序的元素，找到它在序列中适当的位置，并将其插入。 
#  重复直到所有输入数据插入完为止。 
#  
# 
#  下面是插入排序算法的一个图形示例。部分排序的列表(黑色)最初只包含列表中的第一个元素。每次迭代时，从输入数据中删除一个元素(红色)，并就地插入已排序的列表
# 中。 
# 
#  对链表进行插入排序。 
# 
#  
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: head = [4,2,1,3]
# 输出: [1,2,3,4]

# 
#  示例 2： 
# 
#  
# 
#  
# 输入: head = [-1,5,3,4,0]
# 输出: [-1,0,3,4,5] 
# 
#  
# 
#  提示： 
# 
#  
# 
#  
#  列表中的节点数在 [1, 5000]范围内 
#  -5000 <= Node.val <= 5000 
#  
#  Related Topics 链表 排序 
#  👍 535 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        newnode =ListNode(-1)
        cur = newnode
        while head:
            if head.val < cur.val:
                cur = newnode
            #永远不对当前状态进行修改
            while cur.next and head.val > cur.next.val:
                cur = cur.next
            cur_next = cur.next
            cur.next = ListNode(head.val)
            cur.next.next = cur_next
            cur = cur.next
            head = head.next
        return newnode.next
# leetcode submit region end(Prohibit modification and deletion)
