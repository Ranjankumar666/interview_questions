from locale import currency
from linked_list import LinkedList, Node

def bubblesort(head):
    if head is None:
        return head

    i = head

    while i:
        j = i.next

        while j:
            if i.data > j.data:
                t = j.data
                j.data = i.data
                i.data = t

            j = j.next

        i = i.next

    return head

def sortedInsert(head, new):
    '''
        To insert, we will use a helper function sortedInsert() which will return the head of the sorted list after insertion. sortedInsert() accepts a list head and a node as an argument and iterates through the list until it finds an element greater than the node.
    '''
    node = Node(new.data)
    if head is None:
        head = node
        return head
    
    t = head
    p = None

   
    while t:
        if t.data > new.data:
            if p is None:
                head = node
            else:
                p.next = node
            node.next = t
            return head

        p = t
        t = t.next 
    
    p.next = node
    return head

def sort(head):
    if head is None or head.next is None:
        return head

    curr = head
    sorted_head = None

    while curr:
        currNext = curr.next

        #code
        sorted_head = sortedInsert(sorted_head, curr)

        curr = currNext

    return sorted_head

ll = LinkedList()
arr = [3, 2 , 1 , 5, 4, 7]        
for i in arr:
    ll.add(i)

ll.head = sort(ll.head)

ll.print()
                       