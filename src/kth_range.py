class Node:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return Node(key)
    if key == root.key:
        return root  # Reject duplicates
    elif key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def kth_smallest(root, k):
    def inorder(node):
        if node is None:
            return []
        return inorder(node.left) + [node.key] + inorder(node.right)

    sorted_keys = inorder(root)
    if k <= 0 or k > len(sorted_keys):
        raise IndexError("k is out of bounds")
    return sorted_keys[k - 1]

def range_sum_bst(root, low, high):
    if root is None:
        return 0
    if root.key < low:
        return range_sum_bst(root.right, low, high)
    elif root.key > high:
        return range_sum_bst(root.left, low, high)
    else:
        return (root.key +
                range_sum_bst(root.left, low, high) +
                range_sum_bst(root.right, low, high))