class Node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.left = Node(0,0)
        self.right = Node(0,0)
        self.left.next = self.right
        self.right.prev = self.left
        self.tab = {}

    def remove(self,node):
        prev = node.prev
        next = node.next
        prev.next = next
        next.prev = prev

    def insert(self,node):
        prev = self.right.prev
        next = self.right
        prev.next = node
        next.prev = node
        node.prev = prev
        node.next = next

    def get(self, key: int) -> int:
        if key in self.tab:
            #modify Linkedlist
            node = self.tab[key]
            self.remove(node)
            self.insert(node)
            return node.val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.tab:
            self.remove(self.tab[key])
        node = Node(key,value)
        self.tab[key] = node
        self.insert(node)

        if len(self.tab) > self.capacity:
            lru = self.left.next
            self.remove(lru)
            del self.tab[lru.key]

        
