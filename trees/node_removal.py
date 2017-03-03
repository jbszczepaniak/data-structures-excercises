from node import Node

def remove(root, data):
  if root.data > data:
    root.left = remove(root.left, data)
    return root
  elif root.data < data:
    root.right = remove(root.right, data)
    return root
  else:
    return None