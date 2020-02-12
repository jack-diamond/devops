import unittest
from linkedlist import LinkedList
from linkedlist import Node
23
class TestMethods(unittest.TestCase):

    def test_on_empty_list(self):
        '''
        Test on empty list.
        '''
        l = LinkedList()
        self.assertTrue(l.empty())
    
    def test2(self):
        '''
        Test on list of length == 1.
        '''
        l = LinkedList()
        l.insert(1)
        self.assertFalse(l.empty())
    
    def test3(self):
        '''
        Test on list of length > 1.
        '''
        l = LinkedList()
        l.insert(1)
        l.insert(2)
        l.insert(3)
        self.assertFalse(l.empty())

if __name__ == '__main__':
    unittest.main()