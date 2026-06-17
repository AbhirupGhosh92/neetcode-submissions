# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        curr,rp = head,head
        prev = dummy
        dummy.next=head
        cnt = 0
        while cnt < n:
            rp = rp.next
            cnt += 1
        while rp:
            rp = rp.next
            curr = curr.next
            prev = prev.next
        prev.next = prev.next.next
        return dummy.next