# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = [root.val]
        def traverse(node):
            if not node: return
            currDiff = abs(node.val - target)
            if currDiff < abs(closest[0] - target):
                closest[0] = node.val
            traverse(node.left)
            traverse(node.right)
        traverse(root)
        return closest[0]