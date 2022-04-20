from linked_list import LinkedList


def reachAt(head, k):
    i = 1

    if k == 0:
        return None

    t = head
    while i<= k-1:
        t = t.next
        i += 1

    return t

def solution(head, m, n):
    if m >= n:
        return head

    start = reachAt(head, m-1)

    prev = start
    curr = head if start is None else start.next
    next = None

    i = m
    while i <= n:
        next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i +=1

    end = next 
    t = prev

    while True:
        if t.next == start:
            break;
        t= t.next
    
    t.next = end

    if start and start.next:
        start.next = prev   
        return head
    else:
        return prev



    

ll = LinkedList[int]()

for i in range(1, 6):
    ll.add(i)

ll.head = solution(ll.head,1, 2)
ll.print()