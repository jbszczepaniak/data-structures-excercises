from avl import AVLTree
import unittest

class TestAVLTree(unittest.TestCase):
    def test_node_insertion(self):
        avl = AVLTree()
        avl.insert(3)
        avl.insert(5)
        self.assertTrue(avl.root.data == 3)
        self.assertTrue(avl.root.right.data == 5)


if __name__ == '__main__':
    unittest.main()
