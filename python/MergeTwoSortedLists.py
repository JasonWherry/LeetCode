# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        # if both are empty, return Null
        if l1 == None and l2 == None:
            return None
        
        # if one is empty, return the other
        if l1 == None:
            return l2
        
        # if one is empty, return the other
        if l2 == None:
            return l1
        
        # if both are not empty, recursive call(next node of smaller element, other head)
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            
            # returns the next smaller element, with the rest of the sorted list
            return l1
        
        # if both are not empty, recursive call(other head, next node of smaller element)
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            
            # returns the next smaller element, with the rest of the sorted list
            return l2
        