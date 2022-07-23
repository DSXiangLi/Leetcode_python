# 给定一棵二叉树 root，返回所有重复的子树。 
# 
#  对于同一类的重复子树，你只需要返回其中任意一棵的根结点即可。 
# 
#  如果两棵树具有相同的结构和相同的结点值，则它们是重复的。 
# 
#  
# 
#  示例 1： 
# 
#  
# 
#  
# 输入：root = [1,2,3,4,null,2,4,null,null,4]
# 输出：[[2,4],[4]] 
# 
#  示例 2： 
# 
#  
# 
#  
# 输入：root = [2,1,1]
# 输出：[[1]] 
# 
#  示例 3： 
# 
#  
# 
#  
# 输入：root = [2,2,2,3,null,3,null]
# 输出：[[2,3],[3]] 
# 
#  
# 
#  提示： 
# 
#  
#  树中的结点数在[1,10^4]范围内。 
#  -200 <= Node.val <= 200 
#  
#  Related Topics 树 深度优先搜索 哈希表 二叉树 
#  👍 443 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        from collections import defaultdict
        hash = defaultdict(int)
        result = []
        def dfs(root):
            nonlocal hash, result
            if not root:
                return ''
            mid = root.val
            left\
                = dfs(root.left)
            right =dfs(root.right)
            seralize = '{}.{}.{}'.format(mid,left,right)
            hash[seralize]+=1
            if hash[seralize]==2:
                result.append(root)
            return seralize
        dfs(root)
        return result

# leetcode submit region end(Prohibit modification and deletion)
