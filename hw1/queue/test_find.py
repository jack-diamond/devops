import unittest
from queue import Queue

class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test find on empty queue.
        '''
        q = Queue()
        self.assertFalse(q.find(1))

    def test2(self):
        '''
        Test find on non-empty queue with present value.
        '''
        q = Queue()
        q.enqueue(2)
        q.enqueue(1)
        q.enqueue(3)
        self.assertTrue(q.find(1))

    def test3(self):
        '''
        Test find on non-empty queue without value.
        '''
        q = Queue()
        q.enqueue(2)
        q.enqueue(1)
        q.enqueue(3)
        self.assertFalse(q.find(5))

    def test4(self):
        '''
        Test find on empty queue with None value.
        '''
        q = Queue()
        self.assertFalse(q.find(None))

    def test5(self):
        '''
        Test find on non-empty queue with None value.
        '''
        q = Queue()
        q.enqueue(2)
        q.enqueue(1)
        q.enqueue(3)
        self.assertFalse(q.find(None))

if __name__ == '__main__':
    unittest.main()
