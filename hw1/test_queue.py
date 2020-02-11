import unittest
from queue import Queue

class TestMethods(unittest.TestCase):

    def test_enqueue(self):
        q = Queue()
        q.enqueue(1)
        self.assertEqual(q.queue[-1], 1)
        q.enqueue(2)
        self.assertEqual(q.queue[-1], 2)
    
    def test_dequeue(self):
        q = Queue()
        for i in range(3):
            q.enqueue(i)
        self.assertEqual(q.dequeue(), 2)
        self.assertEqual(q.dequeue(), 1)
        self.assertEqual(q.dequeue(), 0)

    def test_traverse(self):
        q = Queue()
        for i in range(5):
            q.enqueue(i)
        self.assertEqual(q.traverse(), [0,1,2,3,4])

    def test_empty(self):
        q = Queue()
        self.assertTrue(q.empty())
        q.enqueue(1)
        self.assertFalse(q.empty())
        q.dequeue()
        self.assertTrue(q.empty())

if __name__ == '__main__':
    unittest.main()
