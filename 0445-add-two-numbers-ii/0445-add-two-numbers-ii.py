# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        
        l1=self.reverseList(l1)
        l2=self.reverseList(l2)
        
        
        l3=self.addTwoNumbers2(l1,l2)
        
        return self.reverseList(l3)
        
        
        
        
        
        
       
    
    
    def addTwoNumbers2(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
   
        dummy = ListNode()
        current = dummy
        carry = 0

        
        while l1 or l2 or carry:
            val1 = l1.val if l1 else 0
            val2 = l2.val if l2 else 0

            total = val1 + val2 + carry
            carry = total // 10
            current.next = ListNode(total % 10)
            current = current.next

            
            if l1:
                l1 = l1.next
            if l2:
                l2 = l2.next

        return dummy.next
    
    
        
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