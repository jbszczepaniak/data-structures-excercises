from node import Node
from node import print_list

def reverse_list_iteratively(root):
    curr = root.next
    root.next = None
    while(curr):
        currnext = curr.next
        curr.next = root
        root = curr
        curr = currnext
    return root

if __name__ == '__main__':
    root = Node(2)
    root.next = Node(4)
    root.next.next = Node(6)
    root.next.next.next = Node(7)
    print_list(root)
    root = reverse_list_iteratively(root)
    print_list(root)



