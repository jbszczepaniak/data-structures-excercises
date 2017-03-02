from node import Node

def remove(root, data):
  if root.data > data:
    remove(root.left, data)
  if root.data < data:
    remove(root.right, data)
  else:
    return root.data