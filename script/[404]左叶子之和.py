# 给定二叉树的根节点 root ，返回所有左叶子之和。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入: root = [3,9,20,null,null,15,7] 
# 输出: 24 
# 解释: 在这个二叉树中，有两个左叶子，分别是 9 和 15，所以返回 24
#  
# 
#  示例 2: 
# 
#  
# 输入: root = [1]
# 输出: 0
#  
# 
#  
# 
#  提示: 
# 
#  
#  节点数在 [1, 1000] 范围内 
#  -1000 <= Node.val <= 1000 
#  
# 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 479 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumOfLeftLeaves(self, root: Optional[TreeNode]) -> int:
        total = 0
        def dfs(root):
            nonlocal total
            if not root:
                return
            if root.left and not root.left.left and not root.left.right:
                total+=root.left.val
            dfs(root.left)
            dfs(root.right)

        dfs(root)
        return total

# leetcode submit region end(Prohibit modification and deletion)
