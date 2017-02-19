class Node(object):
    def __init__(self, data):
        self.data = data
        self.next = None

def print_list(root):
    if root:
        print("{}".format(root.data),end=" ")
        print_list(root.next)

