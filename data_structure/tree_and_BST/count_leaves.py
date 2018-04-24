class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

def count_leaves(root, count, removed_node):
    if root is None:
        return 0
    if root.data == removed_node:
        return 0
    if root.left is None and root.right is None:
        return 1

    return count + count_leaves(root.left, count, removed_node) + count_leaves(root.right, count, removed_node)

def create_node(arr, i, created, root):
    if created[i] is not None:
        return
    created[i] = Node(i)
    if arr[i] == -1:
        root[0] = created[i]
        return

    # If parent is not created, then create parent first
    if created[arr[i]] is None:
        create_node(arr, arr[i], created, root)

    p = created[arr[i]]
    if p.left is None:
        p.left = created[i]
    else:
        p.right = created[i]

def create_tree(arr, n):
    created = [None for i in range(n+1)]
    root = [None]
    for i in range(n):
        create_node(arr, i, created, root)

    return root[0]


def createTree_efficient(arr, n):
    node_arr = []
    root = None
    for i in range(n):
        node_arr.append(Node(i))
    for i in range(n):
        if arr[i] == -1:
            root = node_arr[i]
        else:
            p = node_arr[arr[i]]
            if p.left is None:
                p.left = node_arr[i]
            else:
                p.right = node_arr[i]

    return root

def find_depth(arr, i, depth_array):
    if depth_array[i] != 0:
        return

    if arr[i] == -1:
        depth_array[i] = 1
        return

    if depth_array[arr[i]] == 0:
        find_depth(arr, arr[i], depth_array)

    depth_array[i] = 1 + depth_array[arr[i]]


def find_height(arr, n):
    depth_array = [0 for i in range(n)]
    
    for i in range(n):
        find_depth(arr, i, depth_array)

    ht = depth_array[0]
    for i in range(1, n):
        ht = max(ht, depth_array[i])

    return ht


def main():
    # n = int(raw_input())
    # arr = map(int, raw_input().strip().split(' '))
    # removed_node = int(raw_input())

    n = 5
    arr = [-1, 0, 0, 1, 1]
    removed_node = 2
    
    # root = create_tree(arr, n)
    root = createTree_efficient(arr, n)
        
    print "Total leaves:", count_leaves(root, 0, removed_node)
    print "Height:", find_height(arr, n)

if __name__ == '__main__':
    main()
