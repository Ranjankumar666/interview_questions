
def getLastElement(head):

    t = head

    while t.next:
        t = t.next

    return t

def flatten(head):

    if head is None:
        return head
    
    t = head

    while t:
        if t.child:
            nxtOfT = t.next 
            lastOfChild = getLastElement(t.child)
            lastOfChild.next = nxtOfT
            t.next = t.child
            t.child = None

def flattenDoubly(head):
    if head is None:
        return head

    t = head

    while t:
        if t.child:
            nxtOfT = t.next
            t.child.prev = t 
            lastOfChild = getLastElement(t.child)
            lastOfChild.next = nxtOfT
            
            if(nxtOfT): 
                nxtOfT.prev = lastOfChild
            t.next = t.child
            t.child = None
        
        t = t.next
    
    return head
    
