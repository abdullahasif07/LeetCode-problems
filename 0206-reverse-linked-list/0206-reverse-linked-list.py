# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr_node=head
        
        stack=[]
        while curr_node is not None:
            stack.append(curr_node.val)
            curr_node=curr_node.next
            
        if not stack:
            return None
        
        new_head=ListNode(stack.pop())
        curr_node=new_head
        
        while len(stack)!=0:
            new_node=ListNode(stack.pop())
            curr_node.next=new_node
            curr_node=curr_node.next
            
        return new_head    
        