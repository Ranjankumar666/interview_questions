class Node {
	constructor(data) {
		this.data = data;
		this.next = null;
	}
}

class LinkedList {
	constructor() {
		this.head = null;
	}

	add(x) {
		const node = new Node(x);
		if (!this.head) this.head = node;

		t = this.head;

		while (t.next) t = t.next;
		t.next = node;
	}
}



const reachAt = (head, k) => {
	let i = 1;

	if (k == 0) return None;

	t = head;
	while (i <= k - 1) {
		t = t.next;
		i += 1;
    }
    
	return t;
};


const solution = (head , m ,n ) => {
    if(m >= n)
        return head

    start = reachAt(head, m-1)

    prev = start
    curr = start ? start.next : head
    next = None

    let i = m
    while (i <= n) {
         next = curr.next
        curr.next = prev
        prev = curr
        curr = next
        i +=1
    }
       

    let end = next 
    let t = prev

    while (true) { 
        if (t.next == start)
            break;
        t= t.next
    }
        
    
    t.next = end

    if (start && start.next) {
        start.next = prev   
        return head
    }
       

    return prev
}


const ll = new LinkedList();

Array.from({ length: 5 }, (v, k) => k + 1).forEach((v) => ll.add(v));


