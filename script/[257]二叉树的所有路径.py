# 给你一个二叉树的根节点 root ，按 任意顺序 ，返回所有从根节点到叶子节点的路径。 
# 
#  叶子节点 是指没有子节点的节点。 
#  
# 
#  示例 1： 
# 
#  
# 输入：root = [1,2,3,null,5]
# 输出：["1->2->5","1->3"]
#  
# 
#  示例 2： 
# 
#  
# 输入：root = [1]
# 输出：["1"]
#  
# 
#  
# 
#  提示： 
# 
#  
#  树中节点的数目在范围 [1, 100] 内 
#  -100 <= Node.val <= 100 
#  
#  Related Topics 树 深度优先搜索 字符串 回溯 二叉树 👍 782 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        #注意所有需要判断叶节点，要么通过判断保证不出现左/右节点为空，
        result = []
        def preorder(root, path):
            nonlocal result
            if not root.left and not root.right:
                result.append('->'.join(path+[str(root.val)]))
                return
            if root.left:
                preorder(root.left, path+[str(root.val)])
            if root.right:
                preorder(root.right, path+[str(root.val)])

        preorder(root, [])
        return result
# leetcode submit region end(Prohibit modification and deletion)
