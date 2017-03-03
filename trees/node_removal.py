from node import Node

def remove(root, data):
  if root.data > data:
    return remove(root.left, data)
  elif root.data < data:
    return remove(root.right, data)
  else:
    return root