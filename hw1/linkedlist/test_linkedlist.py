import unittest
from linkedlist import LinkedList
from linkedlist import Node

class TestEmpty(unittest.TestCase):

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

class TestInsert(unittest.TestCase):

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

class TestRemove(unittest.TestCase):

    def test_remove_on_empty_list(self):
        '''
        Edge case coverage
        '''
        l = LinkedList()
        self.assertEqual(l.remove(1), None)
    
    def test_remove_on_list_with_single_variable(self):
        '''
        Function coverage
        '''
        l = LinkedList()
        l.insert(1)
        l.remove(1)
        self.assertEqual(l.traverse(), [])

    def test_remove_on_list_with_multiple_variables(self):
        '''
        Function coverage
        '''
        l = LinkedList()
        l.insert(2)
        l.insert(1)
        l.insert(3)
        l.remove(1)
        self.assertEqual(l.traverse(), [2,3])
    
    def test4(self):
        '''
        Test remove on non-empty linkedlist where value is not
        there.
        '''
        l = LinkedList()
        l.insert(2)
        l.insert(1)
        l.insert(3)
        l.remove(5)
        self.assertEqual(l.traverse(), [2,1,3])

    def test5(self):
        '''
        Test removing None from linkedlist.
        '''
        l = LinkedList()
        l.insert(2)
        l.insert(1)
        l.insert(3)
        self.assertEqual(l.remove(None), None)

class TestTraverse(unittest.TestCase):

    def test_on_empty_list(self):
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