from typing import Any
from linked_list import Node, LinkedList, T
       
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