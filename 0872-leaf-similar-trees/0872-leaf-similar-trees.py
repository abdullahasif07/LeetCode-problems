# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from typing import Optional, List

class Solution:
    def __init__(self):
        self.t1 = []

    def leafSimilar(self, root1: Optional[TreeNode], root2: Optional[TreeNode]) -> bool:
        self.t1 = []
        tree1 = self.tree1_vals(root1)
        
        self.t1 = []
        tree2 = self.tree1_vals(root2)
        
        return tree1 == tree2
        
    def tree1_vals(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        if root.left is None and root.right is None:
            self.t1.append(root.val)
        else:
            self.tree1_vals(root.left)
            self.tree1_vals(root.right)
        return self.t1
