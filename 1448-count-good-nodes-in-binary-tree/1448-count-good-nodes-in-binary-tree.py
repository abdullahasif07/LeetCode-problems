# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        if root == None:
            return None
        else:
            return self.helper(root, root.val)
            
    def helper(self, node: TreeNode, max_val) ->int:   
        if node is None:
                return 0
        
        count = 0
        
        if node.val >= max_val:
            count += 1
            max_val = node.val  
        
        count += self.helper(node.left, max_val)
        count += self.helper(node.right, max_val)
        
        return count 
                