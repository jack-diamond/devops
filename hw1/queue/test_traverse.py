import unittest
from queue import Queue

class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test on empty queue.
        '''
        q = Queue()
        self.assertEqual(q.traverse(), [])
    
    def test2(self):
        '''
        Test on non-empty queue of length == 1.
        '''
        q = Queue()
        q.enqueue(0)
        self.assertEqual(q.traverse(), [0])
    
    def test3(self):
        '''
        Test on non-empty queue of length > 1.
        '''
        q = Queue()
        for i in range(0,5):
            q.enqueue(i)
        self.assertEqual(q.traverse(), [0,1,2,3,4])


if __name__ == '__main__':
    unittest.main()
