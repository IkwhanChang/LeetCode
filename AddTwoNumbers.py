# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        root = ListNode(0)
        head = root
        s,c = 0,0
        while l1 and l2:
            s,c = (l1.val+l2.val+c)%10, (l1.val+l2.val+c)//10
            root.next = ListNode(s)
            l1,l2,root = l1.next, l2.next, root.next
        
        while l1:
            s,c = (l1.val+c)%10, (l1.val+c)//10
            root.next = ListNode(s)
            l1, root = l1.next, root.next
        
        while l2:
            s,c = (l2.val+c)%10, (l2.val+c)//10
            root.next = ListNode(s)
            l2, root = l2.next, root.next
            
        if c != 0:
            root.next = ListNode(c)
            
        return head.next
            
            
            