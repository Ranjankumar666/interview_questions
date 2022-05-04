from math import floor


class PriorityQueue:
    def __init__(self) -> None:
        self.queue = []

    def push(self, x):
        self.queue.append(x)

        i = len(self.queue) -1
        parent = floor((i-1)/2)

        while i >= 0:
            if self.queue[i] < self.queue[parent]:
                self.queue[i], self.queue[parent] = self.queue[parent], self.queue[i]

                i = parent
                parent  = floor((i-1)/2)
            else:
                break


    def pop(self):
        top = self.queue[0]
        n = len(self.queue)
        self.queue[0], self.queue[n-1] = self.queue[n-1], self.queue[0]

        i = 0
        child1=  2*i + 1
        child2 = 2*i + 2

        while i < n:
            if self.queue[child1] < self.queue[i] and self.queue[child2] < self.queue[child2]:

                if self.queue[child1] < self.queue[child2]:
                    self.queue[child1],self.queue[i]= self.queue[i], self.queue[child1]

                    i = child1

                else:
                    self.queue[child2],self.queue[i]= self.queue[i], self.queue[child2]

                    i = child2
                
            elif self.queue[i] < self.queue[child1]:
                    self.queue[child1],self.queue[i]= self.queue[i], self.queue[child1]

                    i = child1
            elif self.queue[i] < self.queue[child2]:
                    self.queue[child2],self.queue[i]= self.queue[i], self.queue[child2]
                    i = child2
            else:
                return top
            
            child1 = 2*i + 1
            child2 = 2*i + 2

        