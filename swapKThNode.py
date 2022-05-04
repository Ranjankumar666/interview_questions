from linked_list import LinkedList

def swapkthnode(head,num,k):
    # return head of new linked list
    #code here
    if k >= num or head is None:
        return head
    
    x = head
    i = 1
    prevX = None
    while i < k:
        prevX = x
        x = x.next
        
        i += 1
        
    y = head
    prev = None
    i = 1
    while i < num - k +1:
        prev = y
        y = y.next
        
        i += 1
        
    xNext = x.next
    yNext = y.next

    y.next = xNext
    x.next = yNext

    if prevX is None:
        head = y
    else:
        prevX.next = y
    
    prev.next = x
    
    return head

ll = LinkedList()
ll.addAll([1 ,2 ,3 ,4, 5])

ll.head = swapkthnode(ll.head, 4, 1)
ll.print()