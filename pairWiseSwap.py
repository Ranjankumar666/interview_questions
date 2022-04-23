from linked_list import LinkedList

def pairWiseSwap( head):
        # code here
        if head is None or head.next is None:
            return head
            
        i = head
        j = head.next
        
        while i and j:
            temp = i.data
            i.data = j.data
            j.data = temp
            
            if i.next and j.next:
                i = i.next.next
                j = j.next.next
            else:
                break
    
        return head

ll = LinkedList[int]()

arr = list(map(int , '1 2 2 4 5 6 7 8'.split(' ')))
ll.addAll(arr)

ll.head = pairWiseSwap(ll.head)

ll.print()



