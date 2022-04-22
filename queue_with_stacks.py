class Queue:
    def __init__(self) -> None:
        self.inp = []
        self.out = []

    def enqueue(self, x):
        self.inp.append(x)
        self.out.append(x)


    def dequeue(self):
        if len(self.out) == 0:
            while len(self.len): 
                self.out.append(self.inp.pop())
        
        return self.out.pop()