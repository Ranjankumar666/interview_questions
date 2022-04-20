from email import header
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
            return
        
        t = self.head

        while t.next:
            t = t.next
        
        t.next = node

    def print(self):
        t = self.head

        while t:
            print(t.data, end=' ')
            t = t.next
       
def findMid(head: Node[Any]):
    if head is None:
        return 

    p1 = head
    p2 = head


    while p2.next and p2.next.next:
        p1 = p1.next
        p2 = p2.next.next

    if (p2.next is None):
        return p1.data

    return p1.next.data

def deleteNode(head: Node[T], k: T):
    if head is None:
        return
    

    t = head
    
    while t.next:
        
        if t.next.data == k:
            break
        
        t = t.next
        
    if t.next and t.next.next:
        t.next = t.next.next
    else:
        t.next = None


linkedList = LinkedList[int]()
linkedList2 = LinkedList[int]()

for i in range(1, 6):
    linkedList.add(i)

for i in [2,4,6,7]:
    linkedList2.add(i)

linkedList2.print()
print(end="\n")
linkedList2.reverse()
linkedList2.print()
# print(findMid(linkedList.head))
# print(findMid(linkedList2.head))