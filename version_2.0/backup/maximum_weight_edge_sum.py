from collections import defaultdict

MOD = 10 ** 9 + 7


class DisjointSet: # note - student need not implement this
   def __init__(self):
       self._size = defaultdict(lambda: 1)
       self._parent = {}

   def __getitem__(self, x):
       parent = self._parent.get(x, x)
       if parent == x:
           return x
       self._parent[x] = self[parent]
       return self._parent[x]

   def merge(self, x, y):
       x, y = sorted([self[x], self[y]], key=self.size)
       self._parent[x] = y
       self._size[y] += self._size[x]

   def size(self, x):
       return self._size[self[x]]


class Solution:
   def solve(self, edges):
       edges.sort(key=lambda x: x[2])  # sort the edges in ascending order
       ds = DisjointSet()  
       print ds
       print "----------"            # use disjointSet for merging vertices
       total = 0
       for source, dest, weight in edges:  # go over every next-smallest edge
           total += ds.size(source) * ds.size(dest) * weight  # add the contribution of that edge
           total %= MOD
           ds.merge(source, dest) 
           print ds      # merge the vertices
       return total

print Solution.solve([[1, 4, 7],
                      [4, 5, 8],
                      [2, 3, 6],
                      [3, 4, 1]])
