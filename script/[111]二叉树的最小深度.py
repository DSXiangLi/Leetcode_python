# 给定一个二叉树，找出其最小深度。 
# 
#  最小深度是从根节点到最近叶子节点的最短路径上的节点数量。 
# 
#  说明：叶子节点是指没有子节点的节点。 
# 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [3,9,20,null,null,15,7]
# 输出：2
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [2,null,3,null,4,null,5,null,6]
# 输出：5
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点数的范围在 [0, 10⁵] 内 
#  -1000 <= Node.val <= 1000 
#  
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 798 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        def dfs(root):
            if not root:
                return 0
            elif not root.left and not root.right:
                return 1
            # buyO 忘记加1
            elif not root.left:
                return dfs(root.right)+1
            elif not root.right:
                return dfs(root.left)+1
            else:
                right=dfs(root.right)
                left=dfs(root.left)
                return min(left, right)+1

        return dfs(root)
# leetcode submit region end(Prohibit modification and deletion)
