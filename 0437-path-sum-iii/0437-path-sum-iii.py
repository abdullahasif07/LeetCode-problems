# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        
        if not root:
            return 0

        def countnodepaths(node, target):
            if not node:
                return 0
            count = 0
            if node.val == target:
                count += 1
            count += countnodepaths(node.left, target - node.val)
            count += countnodepaths(node.right, target - node.val)
            return count

        def traverse(node):
            if not node:
                return 0
            total = countnodepaths(node, targetSum)
            total += traverse(node.left)
            total += traverse(node.right)
            return total

        return traverse(root)


