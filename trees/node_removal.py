from node import Node

def remove(root, data):
  if root.data > data:
    root.left = remove(root.left, data)
    return root
  elif root.data < data:
    root.right = remove(root.right, data)
    return root
  else:
    if root.left and root.right:
      # It is sufficent to swap current root
      # and next node in in-order order,
      # which happens to be min node of right subtree
      to_insert = min_node(root.right)
      data_to_insert = to_insert.data
      root = remove(root, to_insert.data)
      root.data = data_to_insert
      return root

    elif root.left:
      return root.left
    elif root.right:
      return root.right
    else:
      return None

def min_node(root):
  if root.left:
    return min_node(root.left)
  return root
