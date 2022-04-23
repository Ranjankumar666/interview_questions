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
    
    def isEmpty(self) -> bool:
        return self.head == None

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

    
    def beforeTargetK(self,head, k):
        t = head
        i  = 1
        
        while ( i < k):
            t = t.next
            i += 1
        
        return t
        

    def delNode(self,head, n):
        if head is None:
            return
        
        if n == 1:
            head = head.next
            return head
            
        k = self.beforeTargetK(head , n- 1)
        t = k.next
        k.next = t.next

    def addAll(self, arr: list[T]):
        for i in arr:
            self.add(i)
    
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

def getAlternate(head):
    if head is None or head.next is None:
        return head
    
    curr = head
    alt = None
    i = None

    while curr:
        if curr.next is None  :
            break

        temp = curr.next.next
        temp2 = curr.next

        curr.next = temp
        temp2.next = None

        if alt is None:
            alt = temp2
            i = temp2
        else:
            i.next = temp2
            i = temp2

        curr = curr.next   
        
    return alt

def reverse(head):
    if head is None and head.next is None:
        return head
    
    t = head
    
    prev = None
    curr = t
    nxt = None
    
    while curr:
        nxt = curr.next
        curr.next = prev
        prev = curr
        curr =nxt
        
    head = prev

    return head


