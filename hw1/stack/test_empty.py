import unittest
from stack import Stack

class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test on empty stack.
        '''
        stack = Stack()
        self.assertTrue(stack.empty())
    
    def test2(self):
        '''
        Test on non-empty stack.
        '''
        stack = Stack()
        stack.push(1)
        self.assertFalse(stack.empty())
    
    def test3(self):
        '''
        Test after pushing/popping resulting in empty stack.
        '''
        stack = Stack()
        stack.push(1)
        stack.pop()
        self.assertTrue(stack.empty())

    def test4(self):
        '''
        Test after pushing/popping resulting in non-empty stack.
        '''
        stack = Stack()
        stack.push(1)
        stack.pop()
        stack.push(2)
        self.assertFalse(stack.empty())

if __name__ == '__main__':
    unittest.main()