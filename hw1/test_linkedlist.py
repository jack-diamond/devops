import unittest
from linkedlist import LinkedList
from linkedlist import Node

class TestMethods(unittest.TestCase):

    def test_insert(self):
        inst = LinkedList()
        inst.insert(4)
        self.assertEqual(inst.head.data, 4)
        inst.insert(5)
        self.assertEqual(inst.head.data, 4)
        inst.insert(6)
        self.assertEqual(inst.head.data, 4)
    
    def test_remove(self):
        inst = LinkedList()
        for i in range(5):
            inst.insert(i)
        inst.remove(1)
        self.assertEqual(inst.traverse(), [0,2,3,4])
        inst.remove(3)
        self.assertEqual(inst.traverse(), [0,2,4])
    
    def test_remove_not_there(self):
        inst = LinkedList()
        for i in range(5):
            inst.insert(i)
        inst.remove(8)
        self.assertEqual(inst.traverse(), [0,1,2,3,4])
        inst.remove(100)
        self.assertEqual(inst.traverse(), [0,1,2,3,4])

    def test_remove_empty(self):
        inst = LinkedList()
        inst.remove(1)
        self.assertEqual(inst.traverse(), [])

    def test_traverse(self):
        inst = LinkedList()
        temp = []
        for i in range(5):
            temp.append(i)
            inst.insert(i)
        
        self.assertEqual(inst.traverse(), temp)

    def test_traverse_empty(self):
        inst = LinkedList()
        self.assertEqual(inst.traverse(), [])

if __name__ == '__main__':
    unittest.main()