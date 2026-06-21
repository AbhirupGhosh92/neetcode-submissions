# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        def height(root,depth):
            if not root:
                return depth
            else:
                depth += 1
                left = height(root.left,depth)
                right = height(root.right,depth)
                return max(left,right)
        return height(root,0)
        