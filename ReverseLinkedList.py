class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        prev, curr, next = head, head.next, head.next.next
        root = head
        root.next = prev
        
        while curr:
            curr.next = root
            prev.next = next
            root=curr

            curr = next
            if not curr:
                break
            next = next.next
            
        return root