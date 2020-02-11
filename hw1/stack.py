class Stack:
    
    def __init__(self):
        self.stack = []
    
    def empty(self):
        return len(self.stack) == 0
    
    def push(self, value):
        self.stack.append(value)
    
    def pop(self):
        if self.empty():
            raise IndexError('pop(): empty stack')
        return self.stack.pop()