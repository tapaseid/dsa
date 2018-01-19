class Node:
  def __init__(self, data=None):
    self.data = data
    self.next = None

class LinkedList:
  def __init__(self):
    self.head = None
    self.root = None

  def push(self, data):
    if self.root is None:
      self.root = Node(data)
      self.head = self.root
    else:
      node = Node(data)
      self.head.next= node  # makes the connection
      self.head = node  #head move to the next node
  
  def display(self):
    temp = self.root
    while(temp):
      print temp.data,
      temp = temp.next

  def remove(self, x):
   prev = self.root
   if prev is None:
      return

   # first element deletion /special case
   if self.root.data == x:
       self.root  = self.root.next
    
   # rest of the elements
   while prev:
      tmp  =  prev.next
      if tmp is None:
          return

      if tmp.data == x:
         
        print "Removing:{}\n".format(tmp.data)
        tmp = tmp.next
        prev.next = tmp

      prev = prev.next


l = LinkedList()
l.push(2)
l.push(1)
l.push(3)
l.push(6)
l.display()
l.remove(2)
l.display()
l.remove(3)
l.display()
l.remove(6)
l.display()

