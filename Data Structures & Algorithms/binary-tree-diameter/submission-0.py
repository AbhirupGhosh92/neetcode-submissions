# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        ans = 0
        def height(root,depth):
            nonlocal ans
            if not root:
                return 0
            else:
                left = height(root.left,depth)
                right = height(root.right,depth)
                out = 1 + max(left,right)
                ans = max(ans,left + right)
                return out
        height(root,0)
        return ans
