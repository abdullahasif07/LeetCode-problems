from typing import Optional

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def longestZigZag(self, root: Optional[TreeNode]) -> int:
        if root is None:
            return 0

        self.max_count = 0

        def dfs(node, direction, count):
            if node is None:
                return

            self.max_count = max(self.max_count, count)

            if direction == 'left':
                dfs(node.left, 'right', count + 1)
                dfs(node.right, 'left', 1)
            else:
                dfs(node.right, 'left', count + 1)
                dfs(node.left, 'right', 1)

        dfs(root, 'left', 0)
        dfs(root, 'right', 0)
        
        return self.max_count



        