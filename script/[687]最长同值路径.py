# 给定一个二叉树的 root ，返回 最长的路径的长度 ，这个路径中的 每个节点具有相同值 。 这条路径可以经过也可以不经过根节点。 
# 
#  两个节点之间的路径长度 由它们之间的边数表示。 
# 
#  
# 
#  示例 1: 
# 
#  
# 
#  
# 输入：root = [5,4,5,1,1,5]
# 输出：2
#  
# 
#  示例 2: 
# 
#  
# 
#  
# 输入：root = [1,4,5,4,4,5]
# 输出：2
#  
# 
#  
# 
#  提示: 
# 
#  
#  树的节点数的范围是 [0, 10⁴] 
#  -1000 <= Node.val <= 1000 
#  树的深度将不超过 1000 
#  
#  Related Topics 树 深度优先搜索 二叉树 👍 578 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestUnivaluePath(self, root: Optional[TreeNode]) -> int:
        #注意这里需要变量，因为遍历过程中depth会被重制
        ans =0
        def dfs(root):
            nonlocal ans
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            lh, rh = 0,0
            if root.left and root.val == root.left.val:
                lh = left+1
            if root.right and root.val ==root.right.val:
                rh = right+1
            ans = max(ans, lh+rh)
            return max(lh, rh)
        dfs(root)
        return ans



# leetcode submit region end(Prohibit modification and deletion)
