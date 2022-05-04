from typing import Generic, Optional, TypeVar

T = TypeVar('T')


class Node(Generic[T]):
    def __init__(self, x: T) -> None:
        self.data: T = x
        self.left: Optional[Node[T]] = None
        self.right: Optional[Node[T]] = None

class BinarySearchTree(Generic[T]):
    def __init__(self) -> None:
        self.root: Optional[Node[T]] = None
    
    def add(self, x: T):
        node = Node[T](x)

        if self.root is None:
            self.root = node
            return 

        curr = self.root

        while True:
            if curr.data < node.data:
                if curr.left is None:
                    curr.left = node
                    return 
                
                curr = curr.left
            else:
                if curr.right is None:
                    curr.right = node
                    return
                
                curr = curr.right
    
    def reverse(self) -> None:
        if self.root is None:
            return
        
        prev = None
        curr = self.head
        nxt = None

        while curr:
            nxt = curr.next
            curr.next = prev
            prev = curr
            curr = nxt
        
        self.root = prev

    def print(self):
        root = self.root

        if root is None: return []
        res = []
        q = []
        q.append(root)
        
        lvl = 1
        count  = 0
        l = []
        while len(q) > 0:
            node = q.pop(0)
            l.append(node.data)
            count += 1

            if node.left: q.append(node.left)
            if node.right: q.append(node.right)
                
            if lvl == count:
                res.append(l)
                l = []
                lvl = len(q)
                count = 0
            
            
            
            
        for i in res:
            print(i)


    