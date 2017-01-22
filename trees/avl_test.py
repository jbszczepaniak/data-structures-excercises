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

        self.assertEqual(avl.in_order(lambda x: x.data), sorted(numbers))

    # def test_in_order_display_of_heights(self):
    #     avl = AVLTree()
    #     numbers = [1,5,4,2,7,5,3,6,3,5,3,2]
    #     for num in numbers:
    #         avl.insert(num)

    #     self.assertEqual(avl.in_order(lambda x: avl.height(x)), sorted(numbers))

    def test_height_of_chosen_node(self):
        avl = AVLTree()
        numbers = [8,7,6,5,4,3,2,1]
        for num in numbers:
            avl.insert(num)
        self.assertEqual(avl.height(avl.root), 7)
        self.assertEqual(avl.height(avl.root.left), 6)
        self.assertEqual(avl.height(avl.root.left.left), 5)
        self.assertEqual(avl.height(avl.root.left.left.left), 4)

    def test_balances_are_assigned(self):
        avl = AVLTree()
        numbers = [8,7,9,5,6]
        #     8
        #    / \
        #   7   9
        #  /
        # 5
        #  \
        #   6
        for num in numbers:
            avl.insert(num)

        avl.recalculate_balances(avl.root)
        avl.in_order(lambda x: print(x.data, avl.height(x), x.bal_coeff,))

if __name__ == '__main__':
    unittest.main()
