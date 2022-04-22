def mid(head):
    fast = head
    slow = head

    while fast.next and fast.next.next:
        fast = fast.next.next
        slow = slow.next

    if fast.next and fast.next.nest is None:
        return slow
    
    return slow.next

def split(head):
    m = mid()
    left = head
    right = m.next
    m.next = None

    return [left, right]

def _mergeSort(head, end):
    if head is None or head.next is None:
        return head

    left, right = split(head)

    _mergeSort(head, mid)
    _mergeSort(mid, None)

    
