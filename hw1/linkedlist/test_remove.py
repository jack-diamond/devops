import unittest
from linkedlist import LinkedList
from linkedlist import Node
23
class TestMethods(unittest.TestCase):

    def test1(self):
        '''
        Test remove on empty linkedlist.
        '''
        l = LinkedList()
        self.assertEqual(l.remove(1), None)
    
    def test2(self):
        '''
        Test remove on non-empty linkedlist of length == 1.
        '''
        l = LinkedList()
        l.insert(1)
        l.remove(1)
        self.assertEqual(l.traverse(), [])

    def test3(self):
        '''
        Test remove on non-empty linkedlist of length > 1.
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
    

if __name__ == '__main__':
    unittest.main()