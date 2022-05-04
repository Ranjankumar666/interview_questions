def levelOrder(root):
    
    if root is None: return []
    res = []
    q = []
    q.append(root)
    
    lvl = 1
    count  = 0
    l = []
    while len(q) > 0:
        node = q.pop(0)
        l.append(node.val)
        count += 1

        if node.left: q.append(node.left)
        if node.right: q.append(node.right)
            
        if lvl == count:
            res.append(l)
            l = []
            lvl = len(q)
            count = 0
        
        
        
        
    return res