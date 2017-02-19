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

def reverse_list_recursively(root):
    if(root.next):
        new_root = reverse_list_recursively(root.next)
    else:
        return root
    root.next.next = root
    root.next = None
    return new_root

if __name__ == '__main__':
    root = Node(2)
    root.next = Node(4)
    root.next.next = Node(6)
    root.next.next.next = Node(7)
    print("list:")
    print_list(root)
    root = reverse_list_iteratively(root)
    print("\nreversed list iteratively:")
    print_list(root)
    root = reverse_list_recursively(root)
    print("\nreversed list recursively:")
    print_list(root)
    print(" ")



