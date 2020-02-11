import unittest
from linkedlist import LinkedList
from linkedlist import Node

class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test on empty list.
        '''
        l = LinkedList()
        self.assertEqual(l.traverse(), [])

    def test2(self):
        '''
        Test on non-empty list of length == 1.
        '''
        l = LinkedList()
        l.insert(1)
        self.assertEqual(l.traverse(), [1])

    def test3(self):
        '''
        Test on non-empty list of length > 1.
        '''
        l = LinkedList()
        for i in range(10):
            l.insert(i)
        self.assertEqual(l.traverse(), [0,1,2,3,4,5,6,7,8,9])


if __name__ == '__main__':
    unittest.main()