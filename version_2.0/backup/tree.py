class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        
def build_tree(inorder, preorder, inStart, inEnd, mp):
    if inStart>inEnd:
        return

    tnode = Node(preorder[build_tree.preIndex])
    build_tree.preIndex += 1

    if inStart == inEnd:
        return tnode

    # indx = search_index(inorder, inStart, inEnd, tnode.data)
    indx = mp[tnode.data]
    
    tnode.left = build_tree(inorder, preorder, inStart, indx-1, mp)
    tnode.right = build_tree(inorder, preorder, indx+1, inEnd, mp)

    return tnode

def search_index(arr, start, end, val):
    for i in range(start, end+1):
        if arr[i] == val:
            return i

def print_inorder(node):
    if node is None:
        return
    print_inorder(node.left)
    print node.data,
    print_inorder(node.right)



def dfs(root, parent=None):
    if root:
        root.parent = parent
        dfs(root.left, root)
        dfs(root.right, root)

def k_distance(root, target, k):
    dfs(root)

    q = [[target, 0]]
    seen = []
    seen.append(target)

    while q:
        if q[0][1] == k:
            return [ele[0].data for ele in q]
        ele = q.pop(0)

        lst = [ele[0].left, ele[0].right, ele[0].parent]

        for i in lst:
            if i and i not in seen:
                seen.append(i)
                q.append([i, ele[1]+1])

    return []


def zigzag(root):
    res = []
    if root is None:
        return res

    st = []
    tmp = []
    reverse_flag = False
    st.append(root)

    while st:
        node = st.pop()
        res.append(node.data)
        if reverse_flag:
            if node.right:
                tmp.append(node.right)
            if node.left:
                tmp.append(node.left)
        else:
            if node.left:
                tmp.append(node.left)
            if node.right:
                tmp.append(node.right)

        if not st:
            st, tmp = tmp, st
            reverse_flag = not reverse_flag

    return res

def print_sum_path(root, k, res):
    if root is None:
        return
    res.append(root.data)

    print_sum_path(root.left, k, res)
    print_sum_path(root.right, k, res)

    sm = 0
    for i in range(len(res)-1, -1, -1):
        sm += res[i]
        if sm == k:
            print res[i:]

    res.pop(-1)


# return True if there is a k sum path from root
def k_sum_to_leaf(root, k, res):
    if root is None:
        return False
    # print "Root: {}, res: {}".format(root.data, res)
    if root.left is None and root.right is None:
        if k == root.data:
            res.append(root.data)
            return True
        else:
            return False

    if k_sum_to_leaf(root.left, k-root.data, res):
        res.append(root.data)
        return True
    if k_sum_to_leaf(root.right, k-root.data, res):
        res.append(root.data)
        return True

    return False

def print_k_sum_paths_helper(root, k, tmp):
    if root is None:
        return
    tmp.append(root.data)
    if root.left is None and root.right is None:
        if k == root.data:
            print tmp

    print_k_sum_paths_helper(root.left, k-root.data, tmp)
    print_k_sum_paths_helper(root.right, k-root.data, tmp)
    tmp.pop()

def print_k_sum_paths(root, k):
    tmp = []
    print_k_sum_paths_helper(root, k, tmp)


def find_path(root, path, val):
    if root is None:
        return False

    path.append(root.data)

    if root.data == val:
        return True

    if find_path(root.left, path, val) or find_path(root.right, path, val):
        return True

    path.pop(-1)
    return False

def lca(root, n1, n2):

    if root is None:
        return

    path1 = []
    path2 = []

    if not find_path(root, path1, n1) or not find_path(root, path2, n2):
        return

    i = 0
    while i < len(path1) and i < len(path2):
        if path1[i] != path2[i]:
            break
        i += 1

    return path1[i-1] 

def is_node_present(root, node):
    if root is None:
        return False

    if root.data == node:
        return True

    return is_node_present(root.left, node) or is_node_present(root.right, node)

def lca_efficient(root, node1, node2):
    if root is None:
        return None

    if root.data == node1 or root.data == node2:
        return root.data

    lft = lca_efficient(root.left, node1, node2)
    rght = lca_efficient(root.right, node1, node2)

    if lft is None and rght is None:
        return None
    elif lft is not None and rght is None:
        return lft
    elif rght is not None and lft is None:
        return rght
    return root.data


def lca_another(root, n1, n2):
    if is_node_present(root, n1) and is_node_present(root, n2):
        return lca_efficient(root, n1, n2)
    return None


def height(root):
    if root is None:
        return 0

    return max(height(root.left), height(root.right)) + 1

def diameter(root):
    if root is None:
        return 0
    return max(height(root.left) + 1 + height(root.right), max(diameter(root.left), diameter(root.right)))

# Time complexity - O(n^2)
def check_height_balance(root):
    
    if root is None:
        return True

    left_height = height(root.left)
    right_height = height(root.right)

    if abs(left_height - right_height) <= 1 and check_height_balance(root.left) and check_height_balance(root.right):
        return True

    return False

def _helper(root, res):
    if root is None:
        return 0

    lh = _helper(root.left, res)
    rh = _helper(root.right, res)

    if abs(lh - rh) > 1:
        res[0] = False
        # print "Hit!"
    return max(lh, rh) + 1


def is_height_balanced(root):
    if root is None:
        return True
    res = [True]
    _helper(root, res)
    return res[0]

class Solution:
    def __init__(self):
        self.res = []
        self.tmp = []
    
    def pathSum(self, A, B):
        curr = [0]
        self._helper(A, B, curr)
        return self.res
        
    def _helper(self,root, B, curr):
        if root is None:
            return

        curr[0] += root.data
        self.tmp.append(root.data)
        if root.left is not None and root.right is not None and curr[0] == B:
            print "Hit!", self.tmp
            self.res.append(self.tmp)
        if root.left is not None:
            self._helper(root.left, B, curr)
        if root.right is not None:
            self._helper(root.right, B, curr)
        
        self.tmp.pop(-1)
import pdb
def all_sum_paths(root, k, curr, res, tmp):
    if root is None:
        return

    tmp.append(root.data)
    curr[0] += root.data
    print "tmp-start: ", tmp, curr
    if root.left is None and root.right is None and curr[0] == k:
        # pdb.set_trace()
        print "HIT", tmp
        res.append(list(tmp))
    all_sum_paths(root.left, k, curr, res, tmp)
    all_sum_paths(root.right, k, curr, res, tmp)
    curr[0] -= root.data
    tmp.pop(-1)
    print "tmp-end: ", tmp, curr

class BT_to_dll:
    def __init__(self):
        self.head = Node()
        self.curr = None

    def BT_to_DLL(self, root):
        if root is None:
            return
        global head, curr
        self.BT_to_DLL(root.left)

        if self.curr == None:
            self.curr = root
            self.head.right = root
            print "HIT", root.data
        else:
            self.curr.right = root
            root.left = curr
        self.curr = root

        self.BT_to_DLL(root.right)

def serialize(root, arr):
    if root is None:
        arr.append(-1)
        return

    arr.append(root.data)
    serialize(root.left, arr)
    serialize(root.right, arr)

def deserialize(arr):
    if not arr:
        return
    val = arr.pop(0)
    if val == -1:
        return
    root = Node(val)
    root.left = deserialize(arr)
    root.right = deserialize(arr)

    return root


def sum_tree(root):
    if root is None:
        return 0

    l = sum_tree(root.left)
    r = sum_tree(root.right)

    # tmp = root.data
    root.data += l + r

    return root.data


def get_level(root, val, level):
    if root is None:
        return 0

    if root.data == val:
        return level

    lft = get_level(root.left, val, level+1)
    if lft != 0:
        return lft
    return get_level(root.right, val, level+1)

def print_cousins_helper(root, key, level):
    if root is None or level < 2:
        return

    if level == 2:
        if root.left.data == key or root.right.data == key:
            return
        if root.left:
            print root.left.data
        if root.right:
            print root.right.data

    print_cousins_helper(root.left, key, level-1)
    print_cousins_helper(root.right, key, level-1)

def print_cousins(root, key):

    level = get_level(root, key, 1)
    print_cousins_helper(root, key, level)

def is_sibling(root, key1, key2):
    if root is None:
        return False

    if (root.left == key1 and root.right == key2) or (root.left == key2 and root.right == key1):
        return True
    lft = is_sibling(root.left, key1, key2)
    rght = is_sibling(root.right, key1, key2)

    return lft or rght


def is_cousins(root, key1, key2):
    if get_level(root, key1, 1) == get_level(root, key2, 1) and not is_sibling(root, key1, key2):
        return True
    return False

def set_parent_and_burn_status(root, parent=None):
    if root is None:
        return

    root.burn = False
    root.parent = parent
    set_parent_and_burn_status(root.left, root)
    set_parent_and_burn_status(root.right, root)

def time_taken_to_burn(root, leaf_node):
    set_parent_and_burn_status(root)

    q = [[leaf_node, 0]]
    res = 0
    while q:
        target_node, burn_time = q.pop(0)
        target_node.burn = True
        res = max(res, burn_time)
        
        if target_node.left and not target_node.left.burn:
            q.append([target_node.left, burn_time+1])
        if target_node.right and not target_node.right.burn:
            q.append([target_node.right, burn_time+1])
        if target_node.parent and not target_node.parent.burn:
            q.append([target_node.parent, burn_time+1])

    return res

def max_sum_path(root, res):
    if root is None:
        return 0

    lft = max_sum_path(root.left, res)
    rght = max_sum_path(root.right, res)

    if root.left is not None and root.right is not None:
        res[0] = max(res[0], lft, rght, lft + root.data + rght)
        return max(lft, rght) + root.data

    if root.left is None:
        return rght + root.data
    if root.right is None:
        return lft + root.data

def kth_ancestor(root, val, k, res):
    if root is None:
        return None

    if root.data == val:
        return k-1

    lft = kth_ancestor(root.left, val, k, res)
    rght = kth_ancestor(root.right, val, k, res)

    if lft == 0 or rght == 0:
        res[0] = root.data

    if lft is None and rght is None:
        return None
    if lft:
        return lft -1
    if rght:
        return rght -1

def largest_bst(root):

    # need to return (isBST, size, min, max) to check 
    def helper(root):
        if root is None:
            return True, 0, float('inf'), float('-inf')
        l = helper(root.left)
        r = helper(root.right)
        if not l[0] or not r[0] or root.data < l[3] or root.data > r[2]:
            return False, max(l[1], r[1]), 0, 0
        return True, 1 + l[1] + r[1], min(l[2], root.data), max(root.data, r[3])
        
    return helper(root)[1]


def min_root_to_leaf_sum(root):
    if root is None:
        return None

    l = min_root_to_leaf_sum(root.left)
    r = min_root_to_leaf_sum(root.right)

    if l is None and r is None:
        return root.data
    elif l is None:
        return r + root.data
    elif r is None:
        return l + root.data
    else:
        return min(l, r) + root.data    

def iterative_inorder(root):
    if root is None:
        return

    stack = []
    stack.append(root)
    while stack:
        tmp = stack.pop()
        if tmp is None:
            if not stack:
                break
            node = stack.pop()
            print node.data
            stack.append(node.right)
        else:
            stack.append(tmp)
            stack.append(tmp.left)

class TreeNodeWithRandomPointer:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        self.random = None
def inorder_with_random_pointer(root):
    if root is None:
        return

    inorder_with_random_pointer(root.left)
    if root.random is not None:
        rand_val = root.random.data
    else:
        rand_val = None
    print "[{}, {}]".format(root.data, rand_val)
    inorder_with_random_pointer(root.right)

def clone_left_right(root, dct):
    if root is None:
        return

    node = TreeNodeWithRandomPointer(root.data)
    dct[node] = root
    node.left = clone_left_right(root.left, dct)
    node.right = clone_left_right(root.right, dct)

    return node

def clone_random(tree, root, dct):
    if root is None:
        return
    
    root.random = dct[root].random

    clone_random(tree.left, root.left, dct)
    clone_random(tree.right, root.right, dct)
    return root

def clone_tree_with_random_pointer():
    tree = TreeNodeWithRandomPointer(1)
    tree.left = TreeNodeWithRandomPointer(2)
    tree.right = TreeNodeWithRandomPointer(3)
    tree.left.left = TreeNodeWithRandomPointer(4)
    tree.left.right = TreeNodeWithRandomPointer(5)
    tree.random = tree.left.right; 
    tree.left.left.random = tree; 
    tree.left.right.random = tree.right;
    # inorder_with_random_pointer(tree)

    dct = {}
    root = clone_left_right(tree, dct)
    root = clone_random(tree, root, dct)
    return root


class AVLTreeNode:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None
        self.count = 1
        self.height = 1

    def insert(self, val):
        pass

    def left_rotation(self, root):
        tmp = root.right
        subtree = tmp.left
        tmp.left = root
        root.right = subtree

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        tmp.height = 1 + max(self.get_height(tmp.left), self.get_height(tmp.right))
        return tmp

    def right_rotation(self, root):
        tmp = root.left
        subtree = tmp.right
        tmp.right = root
        root.left = subtree

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))
        tmp.height = 1 + max(self.get_height(tmp.left), self.get_height(tmp.right))
        return tmp

    def get_height(self, root):
        if root is None:
            return 0
        return root.height


def longest_consecutive_sequence(root):
    mx_count = [1]
    count_seq(root, 0, 0, mx_count)
    return mx_count[0]

def count_seq(root, count, target, mx_count):
    if root is None:
        return

    if root.data == target:
        count += 1
    else:
        count = 1

    mx_count[0] = max(mx_count[0], count)
    count_seq(root.left, count, root.data+1, mx_count)
    count_seq(root.right, count, root.data+1, mx_count)

import pdb
def kth_smallest(root, k, count, res):
    # pdb.set_trace()
    if root is None:
        return
    kth_smallest(root.left, k, count, res)
    count[0] += 1
    if count[0] == k:
        res[0] = root.data
        return
    kth_smallest(root.right, k, count, res)

def find_largest_in_bst(root):
        if root is None:
            return
        curr = root
        while curr.right:
            curr = curr.right
        return curr.data

def find_second_largest_in_bst(root):
    if root is None or (root.left is None and root.right is None):
        return

    current = root
    while current:
        if current.left and not current.right:
            return find_largest_in_bst(current.left)
        if current.right and not current.right.left and not current.right.right:
                return current.data
        current = current.right

class Solution(object):
    def countNodes(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def get_height(root):
            d = 0
            while root.left:
                d += 1
                root = root.left
            return d
        def exists(m, h, root):
            l, r = 0, 2**h - 1
            for _ in range(h):
                pivot = (l+r)/2
                if m<=pivot:
                    root = root.left
                    r = pivot
                else:
                    root = root.right
                    l = pivot+1
            return root is not None
            
        if root is None:
            return 0
        height = get_height(root)
        if height == 0:
            return 1
        left, right = 1, 2**height - 1
        while left <= right:
            mid = (left+right)/2
            if exists(mid, height, root):
                left = mid+1
            else:
                right = mid-1
        return 2**height - 1 + left

def largest_smaller_in_bst(root, k):
    res = - 1

    while root:
        if root.data < k:
            res = root.data
            root = root.right
        else:
            root = root.left

    return res


def sum_root_to_leaf_numbers(root):

    # result = 0
    # stack = [(root, 0)]
    # while stack:
    #     root, curr_sum = stack.pop()
    #     if root:
    #         curr_sum = curr_sum*10 + root.data
            
    #         if not root.left and not root.right:
    #             result += curr_sum
    #         else:
    #             stack.append((root.left, curr_sum))
    #             stack.append((root.right, curr_sum))
                
    # return result
        
    def sum_numbers(root, sm):
        if not root:
            return
        sm = (sm*10) + root.data

        if not root.left and not root.right:
            print "SM: ", sm
            ans[0] += sm
            return

        sum_numbers(root.left, sm)
        sum_numbers(root.right, sm)
    
    ans = [0]
    sum_numbers(root, 0)
    return ans[0]


def evaluate_expression_tree(root):
    if not root:
        return 0

    if not root.left and not root.right:
        return int(root.data)

    left_val = evaluate_expression_tree(root.left)
    right_val = evaluate_expression_tree(root.right)

    if root.data == '+':
        return left_val + right_val
    elif root.data == '-':
        return left_val - right_val
    elif root.data == '*':
        return left_val * right_val
    elif root.data == '/':
        return left_val / right_val
    
def flatten(A):
    def helper(root):
        if not root:
            return
        temp = root.right
        helper(root.left)
        root.right = root.left
        curr = root
        while curr.right:
            curr = curr.right
        curr.right = temp
        helper(temp)
        root.left = None
    helper(A)
    return A

def construct_bst_from_postorder(preorder):
    if not preorder:
            return None
        
    root = Node(preorder[-1])
    s = [root]
    i = len(preorder) - 2
    while i >= 0:
        node = Node(preorder[i])
        
        tmp = None
        while len(s) and s[-1].data > preorder[i]:
            tmp = s.pop()
        
        if tmp:
            tmp.left = node
        else:
            s[-1].right = node
        
        s.append(node)
        i -= 1
    
    return root

# Given a binary tree A. Check whether it is possible to partition the tree to two trees 
# which have equal sum of values after removing exactly one edge on the original tree.

# Example Input
# Input 1:
#                 5
#                /  \
#               3    7
#              / \  / \
#             4  6  5  6

# Input 2:
#                 1
#                / \
#               2   10
#                   / \
#                  20  2

# Example Output
# Output 1:
#  1

# Output 2:
#  0

def check_equal_partition(A):
    seen = []
    def get_total_sum(root):
        if root is None:
            return 0
        seen.append(root.data + get_total_sum(root.left) + get_total_sum(root.right))
        return seen[-1]
            
    total_sum = get_total_sum(A)
    # print seen
    seen.pop()
    if total_sum % 2 == 0 and int(total_sum/2) in seen:
        return 1
    else:
        return 0

def get_path(root, n, p):
    if root is None:
        return False
    p.append(root.data)
    if root.data == n:
        return True
    if (root.left and get_path(root.left, n, p)) or (root.right and get_path(root.right, n, p)):
        return True
    p.pop()
    return False

def distance(root, n1, n2):
    p1, p2 = [], []
    if not get_path(root, n1, p1) or not get_path(root, n2, p2):
        return -1

    # print "p1: ", p1
    # print "p2: ", p2
    i = 0
    while i < len(p1) and i< len(p2):
        if p1[i] != p2[i]:
            break
        i += 1

    return len(p1) + len(p2) - 2*i

def distance2(root, n1, n2):
    def helper(root):
        if not root:
            return 0

        l = helper(root.left)
        r = helper(root.right)
        if root.data == n1 or root.data == n2:
            if l or r:
                ans[0] = max(l, r)
                return 0
            else:
                return 1
        elif l and r:
            ans[0] = l + r
            return 0
        elif l or r:
            return max(l, r) + 1
        return 0

    ans = [-1]
    helper(root)
    return ans[0]

def inorder_successor_in_bst(root, node):
    if root is None or node is None:
        return None

    # Step1 - check in the right subtree
    if node.right:
        curr = node.right
        while curr.left:
            curr = curr.left
        return curr

    # Step2 - apply search in the bst
    succ = Node()
    while root:
        if root.data < node.data:
            root = root.right
        elif root.data > node.data:
            succ = root
            root = root.left
        else:
            break
    return succ

if __name__ == '__main__':

    '''
    Binary tree:
            1
        2      0
      4   5   6
           7
    '''
    inorder =  [4, 2, 5, 7, 1, 6, 0]
    preorder = [1, 2, 4, 5, 7, 0, 6]
    build_tree.preIndex = 0

    mp = {}
    for i in range(len(inorder)):
        mp[inorder[i]] = i

    root = build_tree(inorder, preorder, 0, len(inorder)-1, mp)
    # print_inorder(root)
    # print

    # print "K distance nodes: ", k_distance(root, root.right.left, 4)
    # print "Zig-zag order: ", zigzag(root)

    # res = []
    # print_sum_path(root, 7, res)
    # print k_sum_to_leaf(root, 7, res)
    # print res

    # print_k_sum_paths(root, 7)

    # obj = Solution()
    # print "All paths: ", obj.pathSum(root, 7)

    # res, tmp, curr = [], [], [0]
    # all_sum_paths(root, 7, curr, res, tmp)
    # print res

    # print lca(root, 4, 7)
    # print lca_another(root, 6, 5)

    # print "Diameter: ", diameter(root)


    #       BST
    #       20
    #   10      30
    #  5  15  25   35
    #             32
    #               34 
    root_bst = Node(20)
    root_bst.left = Node(10)
    root_bst.left.left = Node(5)
    root_bst.left.right = Node(15)
    root_bst.right = Node(30)
    root_bst.right.left = Node(25)
    root_bst.right.right = Node(35)
    root_bst.right.right.left = Node(32)
    root_bst.right.right.left.right = Node(34)


    # print check_height_balance(root_bst)
    # print is_height_balanced(root_bst)

    # obj = BT_to_dll()
    # obj.BT_to_DLL(root)
    # print obj.head
    # while obj.head:
    #   print obj.head.data
    #   obj.head = obj.head.right

    # arr = []
    # serialize(root, arr)
    # print arr

    # root = deserialize(arr)
    # print_inorder(root)
    # print

    # sm = sum_tree(root)
    # print "Sum of all nodes: ", sm
    # print_inorder(root)
    # print


    # print_cousins(root, 6)
    # if is_cousins(root, 5, 6):
    #   print "They are cousins :)"
    # else:
    #   print "They are not cousins :("

    # print time_taken_to_burn(root_bst, root_bst.right.left)
    
    # res = [0]
    # max_sum_path(root, res)
    # print res[0]
    # kth_anstr = [-1]
    # kth_ancestor(root, 7, 4, kth_anstr)
    # print kth_anstr[0]

    # print largest_bst(root)

    # print min_root_to_leaf_sum(root)

    # iterative_inorder(root)

    # rt = clone_tree_with_random_pointer()
    # inorder_with_random_pointer(rt)

    # print longest_consecutive_sequence(root)
    # res = [0]
    # kth_smallest(root_bst, 3, [0], res)
    # print res
    # print find_second_largest_in_bst(root_bst)

    # complete binary tree
    #        1
    #    2       3
    #  4   5    6
    root  = Node(1)
    root.left = Node(2)
    root.right = Node(3)
    root.left.left = Node(4)
    root.left.right = Node(5)
    root.right.left = Node(6)

    # obj = Solution()
    # print obj.countNodes(root)

    # print largest_smaller_in_bst(root_bst, 25)
    # print sum_root_to_leaf_numbers(root)


    # creating a sample tree
    root_expression = Node('+')
    root_expression.left = Node('*')
    root_expression.left.left = Node('5')
    root_expression.left.right = Node('4')
    root_expression.right = Node('-')
    root_expression.right.left = Node('100')
    root_expression.right.right = Node('/')
    root_expression.right.right.left = Node('20')
    root_expression.right.right.right = Node('2')
    # print evaluate_expression_tree(root_expression)


    # res = flatten(root_bst)
    # print res.data

    arr = [1, 7, 5, 50, 40, 10]
    # r = construct_bst_from_postorder(arr)
    def inorder(root):
        if root is None:
            return
        inorder(root.left)
        print root.data
        inorder(root.right)
    # inorder(r)

    # print check_equal_partition(root)

    # print distance(root, 4, 6)
    # print distance2(root, 4, 6)

    # successor = inorder_successor_in_bst(root_bst, root_bst.left.right)
    # successor = inorder_successor_in_bst(root_bst, root_bst.right)
    # successor = inorder_successor_in_bst(root_bst, root_bst.right.left)
    # print successor.data





