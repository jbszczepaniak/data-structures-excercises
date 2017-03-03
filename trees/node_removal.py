from node import Node

def remove(root, data):
  if root.data > data:
    root.left = remove(root.left, data)
    return root
  elif root.data < data:
    root.right = remove(root.right, data)
    return root
  else: # This means that
    if root.left and root.right:
      return
      #i don't know
    elif root.left:
      return root.left
    elif root.right:
      return root.right
    else:
      return None