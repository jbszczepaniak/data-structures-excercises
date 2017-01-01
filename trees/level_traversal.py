from node import Node
from queue import Queue

def level_traversal(root):
    if not root:
        return None

    nodes = Queue()
    level_ordered = []
    nodes.put(root)

    while not nodes.empty():
        curr = nodes.get()

        level_ordered.append(curr.data)

        if curr.left:
            nodes.put(curr.left)
        if curr.right:
            nodes.put(curr.right)

    return level_ordered
