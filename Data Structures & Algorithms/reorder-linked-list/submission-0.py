# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        mid = head
        fp = head

        while fp and fp.next:
            mid = mid.next
            fp = fp.next.next

        prev , curr = None , mid
        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Step 3: Merge two halves
        first, sec = head, prev
        while first != sec:
            next_first = first.next
            first.next = sec
            if next_first == sec:  # odd-length list: stop before overlap
                break
            next_sec = sec.next
            sec.next = next_first
            sec = next_sec
            first = next_first
            

    

       
        


        

