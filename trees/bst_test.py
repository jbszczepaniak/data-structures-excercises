import node
import bst
import unittest

class TestBST(unittest.TestCase):

  def test_insertion(self):
    data = [40,30,20,50,10,15,35,46,24]
    root = node.Node(45)
    for d in data:
      root = bst.insert(d, root)

    self.assertEqual(root.left.left.right.data, 35)
    self.assertEqual(root.left.left.left.right.data, 24)

  def basic_bst(self):
    root = node.Node(20)
    root.left = node.Node(15)
    root.right = node.Node(25)
    root.right.right = node.Node(30)
    root.right.left = node.Node(23)
    root.right.right.right = node.Node(35)
    root.right.left.left = node.Node(22)
    return root

  def test_leaf_deletion(self):
    root = self.basic_bst()
    root = bst.remove(15, root)
    self.assertEqual(root.left, None)

  def test_node_with_only_left_child_deletion(self):
    root = self.basic_bst()
    root = bst.remove(23, root)
    self.assertEqual(root.right.left.data, 22)

  def test_node_with_only_right_child_deletion(self):
    root = self.basic_bst()
    root = bst.remove(30, root)
    self.assertEqual(root.right.right.data, 35)

  def test_node_with_both_children_deletion(self):
    root = self.basic_bst()
    root = bst.remove(25, root)
    self.assertEqual(root.right.data, 30)
    self.assertEqual(root.right.right.data, 35)

if __name__ == '__main__':
  unittest.main()