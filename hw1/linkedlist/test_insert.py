import unittest
from linkedlist import LinkedList
from linkedlist import Node

class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test on empty linkedlist.
        '''
        l = LinkedList()
        l.insert(4)
        self.assertEqual(l.head.data, 4)
    
    def test2(self):
        '''
        Test on non-empty linkedlist and use [4,5,1] to verify
        that it was inserted correctly.
        '''
        l = LinkedList()
        l.insert(4)
        l.insert(5)
        l.insert(1)
        self.assertTrue(l.traverse(), [4,5,1])

    def test3(self):
        '''
        Test that head object does not change after 
        '''

if __name__ == '__main__':
    unittest.main()