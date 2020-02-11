import unittest
from stack import Stack

class TestMethods(unittest.TestCase):
    
    def test1(self):
        '''
        Test pop on non-empty stack
        '''
        stack = Stack()
        stack.push(1)
        self.assertEqual(stack.pop(), 1)
    
    def test2(self):
        '''
        Test pop on empty stack
        '''
        stack = Stack()
        self.assertEqual(stack.pop(), None)


if __name__ == '__main__':
    unittest.main()