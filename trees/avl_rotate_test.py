from avl_rotate import AVLNode, insert_to_avl, height
import unittest
import random
import math

class TestAVLTreeRotation(unittest.TestCase):
    def test_node_insertion_without_rotation(self):
        """
        Tree should look like:
                        50
                      /    \
                    25      75
                   /  \    /  \
                  5   30  60  80
                              / \
                            70  90
        """
        root = AVLNode(50)
        for num in [25, 75, 5, 30, 60, 80, 70, 90]:
            root = insert_to_avl(num, root)
        self.assertTrue(root.right.right.right.data == 90)
        self.assertTrue(root.left.right.data == 30)

    def test_node_insertion_with_single_left_rotation(self):
        """
        Tree after rotation:
            15
           /  \
          10   20
        """
        root = AVLNode(10)
        for num in [15,20]:
            root = insert_to_avl(num, root)
        self.assertTrue(root.data == 15)
        self.assertTrue(root.left.data == 10)
        self.assertTrue(root.right.data == 20)

    def test_node_insertion_with_single_right_rotation(self):
        """
        Tree after rotation:
            5
           /  \
          0   10
        """
        root = AVLNode(10)
        for num in [5,0]:
            root = insert_to_avl(num, root)
        self.assertTrue(root.data == 5)
        self.assertTrue(root.left.data == 0)
        self.assertTrue(root.right.data == 10)

    def test_node_insertion_with_right_left_rotation(self):
        """
        Tree after rotation:
            12
           /  \
          10   15
        """
        root = AVLNode(10)
        for num in [15,12]:
            root = insert_to_avl(num, root)
        self.assertTrue(root.data == 12)
        self.assertTrue(root.left.data == 10)
        self.assertTrue(root.right.data == 15)

    def test_node_insertion_with_left_right_rotation(self):
        """
        Tree after rotation:
            7
           / \
          5   10
        """
        root = AVLNode(10)
        for num in [5,7]:
            root = insert_to_avl(num, root)
        self.assertTrue(root.data == 7)
        self.assertTrue(root.left.data == 5)
        self.assertTrue(root.right.data == 10)


if __name__ == '__main__':
    unittest.main()
