import unittest
from stack import Stack

class TestMethods(unittest.TestCase):

    def test_push(self):
        stack = Stack()
        stack.push(4)
        self.assertEqual(stack.stack[-1], 4)
        stack.push(3)
        self.assertEqual(stack.stack[-1], 3)

    def test_empty(self):
        stack = Stack()
        self.assertTrue(stack.empty())
        stack.push(1)
        self.assertFalse(stack.empty())
    
    def test_pop(self):
        stack = Stack()
        stack.push(1)
        stack.push(2)
        stack.push(3)
        self.assertEqual(stack.pop(), 3)
        self.assertEqual(stack.pop(), 2)
        self.assertEqual(stack.pop(), 1)


if __name__ == '__main__':
    unittest.main()