from typing import Any, Generic, TypeVar

T = TypeVar("T")



class Node(Generic[T]):
    def __init__(self, x: T) -> None:
        super().__init__()
        self.data = x
        self.next = None

class LinkedList(Generic[T]):
    def __init__(self) -> None:
        super().__init__()
        self.head: Node[T] = None
        self.length = 0

    def reverse(self):
        t = self.head

        if t is None:
            return

        prev = None
        curr = t
        next = None

        while curr:
            next = curr.next
            curr.next = prev 
            prev = curr
            curr = next
        
        self.head = prev

    
    def add(self, x: T):
        node = Node[T](x)

        if self.head is None:
            self.head = node;
            self.length = 1
            return
        
        t = self.head

        while t.next:
            t = t.next
        
        t.next = node
        self.length += 1

    def __len__(self):
        return self.length

    def print(self):
        t = self.head

        while t:
            print(t.data, end=' ')
            t = t.next