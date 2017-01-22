from avl import AVLTree
import unittest

class TestAVLTree(unittest.TestCase):
    def test_node_insertion(self):
        avl = AVLTree()
        avl.insert(3)
        avl.insert(5)
        self.assertTrue(avl.root.data == 3)
        self.assertTrue(avl.root.right.data == 5)

    def test_in_order_display(self):
        avl = AVLTree()
        numbers = [1,5,4,2,7,5,3,6,3,5,3,2]
        for num in numbers:
            avl.insert(num)

        self.assertEqual(avl.in_order(), sorted(numbers))

if __name__ == '__main__':
    unittest.main()
