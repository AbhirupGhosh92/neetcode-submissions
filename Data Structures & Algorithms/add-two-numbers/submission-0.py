# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        p1,p2 = l1,l2
        cnt = 0
        temp = 0
        dummy = ListNode()
        while p1 or p2:
            if p1:
                temp += p1.val * (10 ** cnt)
                p1 = p1.next
            if p2:
                temp += p2.val * (10 ** cnt)
                p2 = p2.next
            cnt += 1
        p = dummy
        while temp >= 10:
            p.next = ListNode(temp%10)
            temp = temp//10
            p = p.next
        p.next = ListNode(temp)
        return dummy.next

        
