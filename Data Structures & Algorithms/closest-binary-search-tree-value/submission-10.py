class Solution:
    def closestValue(self, root: Optional[TreeNode], target: float) -> int:
        closest = root.val
        # while node exists (including leaves)
        while root:
            dist = abs(root.val - target)
            # 1st iteration this condition is skipped (same value)
            if dist < abs(closest - target):
                closest = root.val
            # closer value (to target) in left subtree
            if target < root.val:
                root = root.left
            # Go right (target is greater than current)
            elif target > root.val:
                root = root.right
            else:
                return closest
        return closest