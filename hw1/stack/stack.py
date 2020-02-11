class Stack:
    
    def __init__(self):
        self.stack = []
    
    def empty(self):
        return len(self.stack) == 0
    
    def push(self, value):
        if value is not None:
            self.stack.append(value)
    
    def pop(self):
        if not self.empty():
            return self.stack.pop()