# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        tab = 0
        return self.calculate_depth(root,tab)
    
    def calculate_depth(self,root,tab):
        if not root:
            return tab
        else:
            tab += 1
            out1 = self.calculate_depth(root.left,tab)
            out2 = self.calculate_depth(root.right,tab)
            return max(out1,out2)
        