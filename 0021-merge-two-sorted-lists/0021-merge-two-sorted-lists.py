# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        l1=[]
        l2=[]
        curr_node=list1
        while curr_node!=None:
            val=curr_node.val
            l1.append(val)
            curr_node=curr_node.next
            
        curr_node=list2
        while curr_node!=None:
            val=curr_node.val
            l2.append(val)
            curr_node=curr_node.next 
        
        final=sorted(l1+l2)
        
        if not final:
            return None
        
        head=ListNode(final[0])
        curr_node=head
        
        for i in range(1,len(final)):
            newnode=ListNode(final[i])
            curr_node.next=newnode
            curr_node=newnode
        
        return head
            
            
      
        