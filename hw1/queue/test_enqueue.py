import unittest
from queue import Queue

class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test on empty queue.
        '''
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.queue[-1], 1)

    def test2(self):
        '''
        Test on non-empty queue.
        '''
        q = Queue()
        q.enqueue(1)
        q.enqueue(2)
        self.assertEqual(q.queue[-1], 2)
    
    def test3(self):
        '''
        Test with a None object.
        '''
        q = Queue()
        q.enqueue(None)
        self.assertEqual(q.queue, [])
    

if __name__ == '__main__':
    unittest.main()
