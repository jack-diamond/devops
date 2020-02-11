import unittest
from stack import Stack

class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test on empty stack.
        '''
        stack = Stack()
        stack.push(4)
        self.assertEqual(stack.stack[-1], 4)

    def test2(self):
        '''
        Test on non-empty stack.
        '''
        stack = Stack()
        stack.push(4)
        stack.push(3)
        self.assertEqual(stack.stack[-1], 3)

    def test3(self):
        '''
        Test on pushing a None object.
        '''
        stack = Stack()
        stack.push(None)
        self.assertEqual(stack.stack, [])


if __name__ == '__main__':
    unittest.main()