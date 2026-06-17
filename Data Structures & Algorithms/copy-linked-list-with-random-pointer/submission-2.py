"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        #create a table of new nodes
        pt = head
        tab = {}

        while pt:
            tab[pt] = Node(pt.val)
            pt = pt.next
        
        pt=head
        if not head:
            return None
        new_head = tab[head]
        new_pt = new_head
        
        while pt:
            if pt.next:
                new_pt.next = tab[pt.next]
            else:
                new_pt.next = None
            if pt.random:
                new_pt.random = tab[pt.random]
            else:
                new_pt.random = None
            
            pt = pt.next
            new_pt = new_pt.next
        return new_head
