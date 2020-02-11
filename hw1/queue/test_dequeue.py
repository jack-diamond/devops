import unittest
from queue import Queue

class TestMethods(unittest.TestCase):
    
    def test1(self):
        '''
        Test on empty queue.
        '''
        q = Queue()
        self.assertEqual(q.dequeue(), None)
    
    def test2(self):
        '''
        Test on non-empty queue of length == 1.
        '''
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.dequeue(), 1)

    def test3(self):
        '''
        Test on non-empty queue of length > 1.
        '''
        q = Queue()
        for i in range(3):
            q.enqueue(i)
        self.assertEqual(q.dequeue(), 2)


if __name__ == '__main__':
    unittest.main()
