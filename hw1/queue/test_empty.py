import unittest
from queue import Queue

class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test on empty queue.
        '''
        queue = Queue()
        self.assertTrue(queue.empty())
    
    def test2(self):
        '''
        Test on non-empty queue.
        '''
        queue = Queue()
        queue.enqueue(1)
        self.assertFalse(queue.empty())
    
    def test3(self):
        '''
        Test after enqueueing/dequeueing resulting in empty queue.
        '''
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        self.assertTrue(queue.empty())

    def test4(self):
        '''
        Test after enqueueing/dequeueing resulting in non-empty queue.
        '''
        queue = Queue()
        queue.enqueue(1)
        queue.dequeue()
        queue.enqueue(2)
        self.assertFalse(queue.empty())

if __name__ == '__main__':
    unittest.main()