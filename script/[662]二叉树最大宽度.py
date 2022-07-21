# 给定一个二叉树，编写一个函数来获取这个树的最大宽度。树的宽度是所有层中的最大宽度。这个二叉树与满二叉树（full binary tree）结构相同，但一些节
# 点为空。 
# 
#  每一层的宽度被定义为两个端点（该层最左和最右的非空节点，两端点间的null节点也计入长度）之间的长度。 
# 
#  示例 1: 
# 
#  
# 输入: 
# 
#            1
#          /   \
#         3     2
#        / \     \  
#       5   3     9 
# 
# 输出: 4
# 解释: 最大值出现在树的第 3 层，宽度为 4 (5,3,null,9)。
#  
# 
#  示例 2: 
# 
#  
# 输入: 
# 
#           1
#          /  
#         3    
#        / \       
#       5   3     
# 
# 输出: 2
# 解释: 最大值出现在树的第 3 层，宽度为 2 (5,3)。
#  
# 
#  示例 3: 
# 
#  
# 输入: 
# 
#           1
#          / \
#         3   2 
#        /        
#       5      
# 
# 输出: 2
# 解释: 最大值出现在树的第 2 层，宽度为 2 (3,2)。
#  
# 
#  示例 4: 
# 
#  
# 输入: 
# 
#           1
#          / \
#         3   2
#        /     \  
#       5       9 
#      /         \
#     6           7
# 输出: 8
# 解释: 最大值出现在树的第 4 层，宽度为 8 (6,null,null,null,null,null,null,7)。
#  
# 
#  注意: 答案在32位有符号整数的表示范围内。 
#  Related Topics 树 深度优先搜索 广度优先搜索 二叉树 👍 384 👎 0


# leetcode submit region begin(Prohibit modification and deletion)
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        maxw = 0
        stack = [(root,0)]
        while stack:
            l = len(stack)
            left = 0
            for i in range(l):
                node, pos = stack.pop(0)
                if i==0:
                    left= pos
                if node.left:
                    stack.append((node.left, pos*2))
                if node.right:
                    stack.append((node.right, pos*2+1))
                if i==l-1:
                    maxw = max(maxw, pos-left+1)
        return maxw



# leetcode submit region end(Prohibit modification and deletion)
