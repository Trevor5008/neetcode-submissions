class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        self.closest = root.val
        def traverse(node):
            if not node: return
            currDiff = abs(node.val - target)
            bestDiff = abs(self.closest - target)
            if currDiff < bestDiff or currDiff == bestDiff:
                self.closest = node.val
            if node.val > target:
                traverse(node.left)
            elif node.val < target:
                traverse(node.right)
        traverse(root)
        return self.closest