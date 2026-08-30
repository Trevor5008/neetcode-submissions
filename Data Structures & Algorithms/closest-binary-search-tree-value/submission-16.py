class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        if root.val == target:
            return root.val
        closest = root.val
        def traverse(node):
            nonlocal closest
            if not node:
                return 
            
            if abs(node.val - target) < abs(closest - target):
                closest = node.val
            elif abs(node.val - target) == abs(closest - target):
                closest = min(closest, node.val)
            
            if target < node.val:
                traverse(node.left)
            else:
                traverse(node.right)
        traverse(root)
        return closest