class Queue:

    def __init__(self):
        self.queue = []

    def enqueue(self, value):
        if value is not None:
            self.queue.append(value)
    
    def dequeue(self):
        if self.empty():
            return
        return self.queue.pop()
    
    def traverse(self):
        return [i for i in self.queue]

    def find(self, value):
        if value in self.queue:
            return True
        return False

    def empty(self):
        if len(self.queue) == 0:
            return True
        return False
