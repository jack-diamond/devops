class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        self.queue.append(value)
    
    def dequeue(self):
        return self.queue.pop()
    
    def traverse(self):
        return [i for i in self.queue]

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False
