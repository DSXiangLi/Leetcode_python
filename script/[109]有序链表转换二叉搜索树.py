# 给定一个单链表的头节点 head ，其中的元素 按升序排序 ，将其转换为高度平衡的二叉搜索树。 
# 
#  本题中，一个高度平衡二叉树是指一个二叉树每个节点 的左右两个子树的高度差不超过 1。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入: head = [-10,-3,0,5,9]
# 输出: [0,-3,9,-10,null,5]
# 解释: 一个可能的答案是[0，-3,9，-10,null,5]，它表示所示的高度平衡的二叉搜索树。
#  
# 
#  示例 2: 
# 
#  
# 输入: head = []
# 输出: []
#  
# 
#  
# 
#  提示: 
# 
#  
#  head 中的节点数在[0, 2 * 10⁴] 范围内 
#  -10⁵ <= Node.val <= 10⁵ 
#  
#  Related Topics 树 二叉搜索树 链表 分治 二叉树 👍 730 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sortedListToBST(self, head: Optional[ListNode]) -> Optional[TreeNode]:
        def dfs(start, end):
            nonlocal head
            if start>end:
                return None
            mid = (start+end)//2

            left= dfs(start, mid-1)
            root = TreeNode(head.val)
            head = head.next
            right = dfs(mid+1, end)
            root.left = left
            root.right = right
            return root
        counter = 0
        cur = head
        while cur:
            cur = cur.next
            counter+=1
        return dfs(1, counter)
# leetcode submit region end(Prohibit modification and deletion)
