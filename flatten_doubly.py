
def getLastElement(head):

    t = head

    while t.next:
        t = t.next

    return t


def flatten(head):

    t = head

    while t:
        if t.child:
            temp1 = t.next
            x = getLastElement(t.child)
            x.next = temp1
            t.next = x
            t.child = None
        
        t = t.next
    
    return head