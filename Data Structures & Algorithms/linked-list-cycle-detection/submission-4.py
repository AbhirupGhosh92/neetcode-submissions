# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        if not head:
            return False
        sp = head
        fp = head
        while sp.next and fp.next and fp.next.next:
            if sp.next == fp.next.next:
                return True
            else:
                sp = sp.next
                fp = fp.next.next
        return False
    