# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root: return 0
        maxDepth = [0]
        def traverse(node, depth=1):
            if not node:
                return
            traverse(node.left, depth+1)
            maxDepth[0] = max(maxDepth[0], depth)
            traverse(node.right, depth+1)
        traverse(root)
        return maxDepth[0]
