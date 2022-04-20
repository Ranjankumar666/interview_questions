from linked_list import LinkedList

def getKthNode(head, k):
    t = head
    i = 1
    if k == 1:
        return head

    while i <= k-1:
        t = t.next
        i += 1
    return t

def getLength(head):
    t = head
    i = 0

    if t is None:
        return 0


    while t:
        i += 1
        t = t.next
        
    return i

def rotate(head, k):
        # code here
        n = getLength(head)
        if k < 1 or k >= getLength(head) : 
            return head
            
        x = getKthNode(head, k)
        t1 = x.next
        p = t1
        x.next = None

        while p.next:
            p = p.next
        
        p.next = head

        return t1
        

ll = LinkedList[int]()

arr = list(map(int, '1 2 3 4 5 6 7 8'.split(' ')))

for i in arr:
    ll.add(i)

ll.head  = rotate(ll.head, 4)

ll.print()