# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, l1: ListNode, l2: ListNode) -> ListNode:
        combined = ListNode(0)
        head = combined
        while l1 and l2:
            if l1.val < l2.val:
                combined.next = l1
                l1, combined = l1.next, combined.next
            else:
                combined.next = l2
                l2, combined = l2.next, combined.next
                
        while l1:
            combined.next = l1
            l1, combined = l1.next, combined.next
            
        while l2:
            combined.next = l2
            l2, combined = l2.next, combined.next
            
        return head.next