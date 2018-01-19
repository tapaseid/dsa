# Red-Black Tree is a self-balancing Binary Search Tree (BST)
# where every node follows following rules:

# 1) Every node has a color either red or black.
# 2) Root of tree is always black.
# 3) There are no two adjacent red nodes (A red node cannot have a red parent or red child).
# 4) Every path from root(every node as a root) to a NULL node has same number of black nodes.


# Time complexity
# ---------------
# Insert ---> O(log n)
# Delete ---> O(log n)
#
# Does not work for duplicates


COLOR = ["RED", "BLACK"]

class RBTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.parent = None
        self.color = COLOR[0]

class Red_Black_Tree:
    def insert(self, root, key):

        node = RBTreeNode(key)
        
        root = self.BST_insert(root, node)

        #Logic for red-black tree
        self.fix_Violation(root, node)

        return root

    def BST_insert(self, root, node):
        # Base case, and check for root node.
        if root is None:
            return node

        if node.data < root.data:
            root.left = self.BST_insert(root.left, node)
            root.left.parent = root

        else:
            root.right = self.BST_insert(root.right, node)
            root.right.parent = root

        return root

    def delete(self, root, key):
        if root is None:
            return

        if key < root.data:
            root.left = self.delete(root.left, key)
        if key > root.data:
            root.right = self.delete(root.right, key)
        else:
            if root.left is None:
                temp = root.right
                root = None
                return temp
            if root.right is None:
                temp = root.left
                root = None
                return temp
            
            temp = self.getMinValueNode(root.right)
            root.data = temp.data
            root.right = self.delete(root.right, temp.data)

        # Logic for red-black tree
        root = self.fix_Violation(root)

        return root

    def fix_Violation(self, root, node):

        while(node is not root and node.color is not COLOR[1] and node.parent.color is COLOR[0]):
            parent_pt = node.parent
            grand_parent = parent_pt.parent

            # Case-A: Parent of root is left child of Grand-parent of root
            if parent_pt == grand_parent.left:
                uncle_pt = grand_parent.right

                # Case 1: when uncle is also red, recoloring required
                if uncle_pt is not None and uncle_pt.color==COLOR[0]:
                    parent_pt.color = COLOR[1]
                    uncle_pt.color = COLOR[1]
                    grand_parent.color = COLOR[0]

                else:
                    # Case 2: root is right child if it's parent, left-rotation required
                    if node == parent_pt.right:
                        node = self.leftRotate(root, parent_pt)
                        node.parent = grand_parent

                    # Case 3: root is left child if it's parent, right-rotation required
                    node = self.rightRotate(root, grand_parent)
                    grand_parent.parent = root
                    node.color, grand_parent.color = grand_parent.color, node.color

            # Case-B: Parent of root is right child of Grand-parent of root
            else:
                uncle_pt = grand_parent.left

                # Case 1: when uncle is also red, recoloring required
                if uncle_pt is not None and uncle_pt.color==COLOR[0]:
                    parent_pt.color = COLOR[1]
                    uncle_pt.color = COLOR[1]
                    grand_parent.color = COLOR[0]

                else:
                    # Case 2: root is left child if it's parent, right-rotation required
                    if node == parent_pt.left:
                        node = self.rightRotate(root, parent_pt)
                        node.parent = grand_parent

                    # Case 3: root is right child if it's parent, left-rotation required
                    node = self.leftRotate(root, grand_parent)
                    grand_parent.parent = root
                    node.color, grand_parent.color = grand_parent.color, node.color

        root.color = COLOR[1]

    def findUncleNode(self, node):
        p = node.parent
        if p.parent:
            if p.parent.left == p:
                return p.parent.right
            else:
                return p.parent.left
        else:
            return None

    def findSiblingNode(self, node):
        p = node.parent
        if p.left == node:
            return p.right
        else:
            return p.left

    def leftRotate(self, root, x):
        y = x.right
        T2 = y.left

        y.left = x
        x.right = T2

        # Logic for red-black tree
        x.parent = y
        if T2:
            T2.parent = x

        return y

    def rightRotate(self, root, x):
        y = x.left
        T3 = y.right

        y.right = x
        x.left = T3

        # Logic for red-black tree
        x.parent = y
        if T3:
            T3.parent = x

        return y

    def getMinValueNode(self, root):
        current = root
        while current.left is not None:
            current = current.left
        return current

    def inOrder(self, root):
        if root is None:
            return

        self.inOrder(root.left)
        print "{}({})".format(root.data, root.color),
        self.inOrder(root.right)

    def levelOrder(self, root):
        if root is None:
            return

        qu = []
        qu.append(root)
        while qu:
            p = qu.pop(0)
            print "{}({})".format(p.data, p.color),
            if p.left:
                qu.append(p.left)
            if p.right:
                qu.append(p.right)

if __name__ == '__main__':
    rb_tree = Red_Black_Tree()
    root = None
    arr = [10, 20, 30, 40, 50, 25, 35]
    for i in arr:
        root = rb_tree.insert(root, i)
        rb_tree.levelOrder(root)
        print

    # rb_tree.inOrder(root)
    # rb_tree.levelOrder(root)
    # rb_tree.delete(root, 20)
    # print 
    # rb_tree.inOrder(root)
    # rb_tree.levelOrder(root)
