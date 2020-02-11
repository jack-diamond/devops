import unittest
from linkedlist import LinkedList
from linkedlist import Node

class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test on empty list.
        '''
        l = LinkedList()
        self.assertFalse(l.find(1))

    def test2(self):
        '''
        Test on list of length == 1 with value not present.
        '''
        l = LinkedList()
        l.insert(2)
        self.assertFalse(l.find(1))
    
    def test3(self):
        '''
        Test on list of length == 1 with value present.
        '''
        l = LinkedList()
        l.insert(2)
        self.assertTrue(l.find(2))
    
    def test4(self):
        '''
        Test on list of length > 1 with value not present.
        '''
        l = LinkedList()
        l.insert(2)
        l.insert(1)
        l.insert(3)
        self.assertFalse(l.find(4))
    
    def test5(self):
        '''
        Test on list of length > 1 with value present.
        '''
        l = LinkedList()
        l.insert(2)
        l.insert(1)
        l.insert(3)
        self.assertTrue(l.find(1))


if __name__ == '__main__':
    unittest.main()