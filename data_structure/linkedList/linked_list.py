# Linked list

class Node:
    def __init__(self, data=None):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.count = 0

    def push(self, new_data):
        new_node = Node(new_data)
        new_node.next = self.head
        self.head = new_node
        self.count += 1

    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print "The previous node must be in linked list!"
            return

        new_node = Node(new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        self.count += 1
    
    def append(self, new_data):
        new_node = Node(new_data)

        if self.head is None:
            self.head = new_node
            self.count += 1
            return

        last = self.head
        while(last.next):
            last = last.next

        last.next = new_node
        self.count += 1      

    def deleteNode(self, key):
        temp = self.head

        if temp is not None:
            if temp.data == key:
                self.head = temp.next
                temp = None
                self.count -= 1
                return

        while(temp is not None):
            if temp.data == key:
                break
            prev = temp
            temp = temp.next

        if temp is None:
            print "Key is not present in the linked list!"
            return

        prev.next = temp.next
        temp = None
        self.count -= 1   

    def deleteNodeAtPos(self, position):
        if self.head is None:
            return

        temp = self.head

        if position == 0:
            self.head = temp.next
            temp = None
            self.count -= 1
            return

        for i in range(1, position+1):
            if temp.next is not None:
                prev = temp
                temp = temp.next
            else:
                print "position out of bound!"
                return

        prev.next = temp.next
        temp = None
        self.count -= 1       

    def swapNodes(self, x, y):
        if x == y:
            return
        
        prevX = None
        currX = self.head
        while currX != None and currX.data != x:
            prevX = currX
            currX = currX.next

        prevY = None
        currY = self.head
        while currY != None and currY.data != y:
            prevY = currY
            currY = currY.next

        if currX == None or currY == None:
            return

        if prevX != None:
            prevX.next = currY
        else:
            self.head = currY

        if prevY!= None:
            prevY.next = currX
        else:
            self.head = currX

        # import pdb
        # pdb.set_trace()
        temp = currX.next
        currX.next = currY.next
        currY.next = temp

    def reverse_iterative(self):
        prev = None
        current = self.head
        while(current is not None):
            next = current.next
            current.next = prev
            prev = current
            current = next
        self.head = prev

    def reverse(self):
        if self.head is None:
            return
        self.reverseUtil(self.head, None)

    def reverseUtil(self, curr, prev):
        if curr.next is None:
            self.head = curr
            curr.next = prev
            return
        
        next = curr.next
        curr.next = prev
        self.reverseUtil(next, curr)

    def reverseGroup(self, head, k):
        current = head
        next = None
        prev = None
        count = 0

        while(current is not None and count < k):
            next = current.next
            current.next = prev
            prev = current
            current = next
            count +=1

        if next is not None:
            head.next = self.reverseGroup(next, k)

        return prev

    def getCount(self):
        temp = self.head
        count = 0
        while(temp):
            count += 1
            temp = temp.next
        return count    

    def detectAndRemoveLoop(self):
        slow_p = fast_p = self.head
        while(slow_p and fast_p and fast_p.next):
            slow_p = slow_p.next
            fast_p = fast_p.next.next
            if slow_p == fast_p:
                self.removeLoop_efficient(slow_p)
                return 1
        return 0

    def removeLoop(self, loop_node):
        ptr1 = self.head
        while(1):
            ptr2 = loop_node
            while(ptr2.next != loop_node and ptr2.next != ptr1):
                ptr2 = ptr2.next
            if ptr2.next == ptr1:
                break
            ptr1 = ptr1.next
        ptr2.next = None

    def removeLoop_better1(self, loop_node):
        ptr1 = loop_node
        k = 1
        while ptr1.next != loop_node:
            ptr1 = ptr1.next
            k += 1

        ptr1 = ptr2 = self.head
        for i in range(k):
            ptr2 = ptr2.next

        while(ptr1 != ptr2):
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        while ptr2.next != ptr1:
            ptr2 = ptr2.next
        ptr2.next = None

    def removeLoop_efficient(self, loop_node):
        ptr1 = self.head
        ptr2 = loop_node
        while ptr1.next != ptr2.next:
            ptr1 = ptr1.next
            ptr2 = ptr2.next

        ptr2.next = None


    def addTwoLists(self, h1, h2):
        prev = None
        temp = None
        carry = 0

        while(h1 is not None or h2 is not None):
            fdata = 0 if h1 is None else h1.data
            sdata = 0 if h2 is None else h2.data
            Sum = carry + fdata + sdata
            carry = 1 if Sum > 10 else 0
            Sum = Sum if Sum < 10 else Sum%10
            temp = Node(Sum)

            if self.head is None:
                self.head = temp
            else:
                prev.next = temp
            prev = temp

            if h1 is not None:
                h1 = h1.next
            if h2 is not None:
                h2 = h2.next

        if carry > 0:
            temp.next = Node(carry)


    def rotate(self, k):
        if k == 0:
            return

        current = self.head
        count = 1
        while(count<k and current is not None):
            current = current.next
            count += 1
        if current is None:
            return

        kthNode = current
        while current.next is not None:
            current = current.next

        current.next = self.head
        self.head = kthNode.next
        kthNode.next = None


    def printList(self):
        temp = self.head
        while(temp):
            print temp.data,
            temp = temp.next
        print ''    


def sortedMerge_recursion(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    if h1.data < h2.data:
        h1.next = sortedMerge_recursion(h1.next, h2)
        return h1
    else:
        h2.next = sortedMerge_recursion(h1, h2.next)
        return h2

def sortedMerge_iteration(h1, h2):
    if h1 is None:
        return h2
    if h2 is None:
        return h1

    s = t = Node()
    while not (h1 is None or h2 is None):
        if h1.data < h2.data:
            t.next = h1
            h1 = h1.next
        else:
            t.next = h2
            h2 = h2.next
        t = t.next

    t.next = h1 or h2
    return s.next



if __name__=='__main__':
    llist = LinkedList()
    # llist.head = Node(1)
    # second = Node(2)
    # third = Node(3)

    # llist.head.next = second
    # second.next = third

    # llist.printList()

    llist.append(6)
    llist.push(7)
    llist.push(1)
    llist.append(4)

    llist.insertAfter(llist.head.next, 8)
    print "Created Linked list:",
    llist.printList()
    print "Count:", llist.count

    print "Reverse as group:",
    llist.head = llist.reverseGroup(llist.head, 3)
    llist.printList()

    llist.deleteNodeAtPos(2)
    print "After deleting a node:",
    llist.printList()
    print "Count:", llist.count

    llist.swapNodes(7, 4)
    print "After swaping:",
    llist.printList()

    llist.reverse()
    print "Reversed:",
    llist.printList()


    #merge two linked lists
    l1 = LinkedList()
    l1.push(5)
    l1.push(3)
    l1.push(1)

    l2 = LinkedList()
    l2.push(4)
    l2.push(2)
    print "L1:",
    l1.printList()
    print "L2:",
    l2.printList()
    l = LinkedList()

    l.addTwoLists(l1.head, l2.head)
    print "Adding two lists:",
    l.printList()

    l.head = sortedMerge_iteration(l1.head, l2.head)
    # l.head = sortedMerge_recursion(l1.head, l2.head)
    l.printList()

    l.head.next.next.next.next.next = l.head.next
    if l.detectAndRemoveLoop():
        print "YES! There is a loop, removing this..."
    else:
        print "NO! There is no loop, carry on!"
    l.printList()
    l.rotate(1)
    l.printList()
