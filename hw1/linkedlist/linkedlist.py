class Node:

    def __init__(self, data=0, next_node=None):
        self.data = data
        self.next = next_node

class LinkedList:

    def __init__(self):
        self.head = None

    def insert(self, value):
        node = Node(value)

        if not self.head:
            self.head = node
            return

        current = self.head
        while current.next:
            current = current.next
        
        current.next = node

    def remove(self, value):
        if value is None:
            return
            
        if not self.head:
            return

        current = self.head
        if self.head.data == value:
            self.head = self.head.next
            current = None
        
        while current:
            if current.data == value:
                break
            prev = current
            current = current.next
        
        if not current:
            return
        
        prev.next = current.next
        current = None


    def traverse(self):
        if not self.head:
            return []
        
        result = []
        current = self.head
        while current:
            result.append(current.data)
            current = current.next
        
        return result

    def find(self, value):
        l = self.traverse()
        if value in l:
            return True
        return False