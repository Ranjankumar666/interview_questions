from linked_list import LinkedList

def removeDuplicates(head):
    if head is None:
        return
    
    mp = set()
    t = head
    prev = None
    
    while(t):
        next = t.next

        if t.data in mp:
            temp = t.next
            prev.next = temp
            
        else:
            mp.add(t.data)
            prev = t

        t = next
        
    
    if prev.data in mp:
        prev = None

ll = LinkedList()
arr = [1 , 2, 3, 4, 5, 5, 5]

for i in arr:
    ll.add(i)

removeDuplicates(ll.head)
ll.print()