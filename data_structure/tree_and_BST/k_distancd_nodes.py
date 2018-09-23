# print nodes at distance k from a given node  

class Node: 
    def __init__(self, data): 
        self.data = data 
        self.left = None
        self.right = None

def printkDistanceNodeDown(root, k): 
    if root is None or k< 0 : 
        return 
    if k == 0 : 
        print root.data  
        return 

    printkDistanceNodeDown(root.left, k-1) 
    printkDistanceNodeDown(root.right, k-1) 

# Prints all nodes at distance k from a given target node 
# The k distant nodes may be upward or downward. This function 
# returns distance of root from target node, it returns -1  
# if target node is not present in tree rooted with root 

def printkDistanceNode(root, target, k): 
    if root is None: 
        return -1

    if root == target: 
        printkDistanceNodeDown(root, k) 
        return 0 

    # Recur for left subtree 
    dl = printkDistanceNode(root.left, target, k) 

    # Check if target node was found in left subtree 
    if dl != -1: 
        # If root is at distance k from target, print root 
        # Note: dl is distance of root's left child from target 
        if dl +1 == k : 
            print root.data 

        # Else go to right subtreee and print all k-dl-2 distant nodes  
        # Note: that the right child is 2 edges away from left chlid 
        else: 
            printkDistanceNodeDown(root.right, k-dl-2) 

        # Add 1 to the distance and return value for 
        # for parent calls  
        return 1 + dl 

    # MIRROR OF ABOVE CODE FOR RIGHT SUBTREE 
    # Note that we reach here only when node was not found 
    # in left subtree 
    dr = printkDistanceNode(root.right, target, k) 

    if dr != -1: 
        if (dr+1 == k): 
            print root.data 
        else: 
            printkDistanceNodeDown(root.left, k-dr-2) 
        return 1 + dr 

    # If target was neither present in left nor in right subtree 
    return -1

  
# Driver program to test above function 
if __name__ == '__main__':
    root = Node(20) 
    root.left = Node(8) 
    root.right = Node(22) 
    root.left.left = Node(4) 
    root.left.right = Node(12) 
    root.left.right.left = Node(10) 
    root.left.right.right = Node(14) 
    target = root.left.right 
    printkDistanceNode(root, target, 2) 
