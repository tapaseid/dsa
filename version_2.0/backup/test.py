
# Rearrange the array
def rearrange(arr):
    n = len(arr)
    tmp = [None]*n
    i, j = 0, n-1
    flag = True
    for k in range(n):
        if flag:
            tmp[k] = arr[j]
            j -= 1
        else:
            tmp[k] = arr[i]
            i += 1
        flag = bool(1-flag)
    return tmp

# print rearrange([1, 2, 3, 4, 5, 6])


# Try BFS, DFS AND Toplogical sort
from collections import defaultdict
class Graph:
    def __init__(self, size):
        self.size = size
        self.graph = defaultdict(list)
        
    def add_edge(self, u, v):
        self.graph[u].append(v)
        
    def bfs(self):
        pass
    
    def dfs(self):
        visited = [False]*self.size

        for node in range(self.size):
            if not visited[node]:
                self.dfs_util(node, visited)
        print
    
    def dfs_util(self, node, visited):
        visited[node] = True
        print node,
        for i in self.graph[node]:
            if not visited[i]:
                self.dfs_util(i, visited)


    def topological(self, v):
        visited = [False]*self.size
        stack = []
        # self.topo_util(v, visited, stack)
        # print "Stack: ", stack
        for node in range(self.size):
            if not visited[node]:
                self.topo_util(node, visited, stack)
        print stack
    
    def topo_util(self, node, visited, stack):
        visited[node] = True
        for i in self.graph[node]:
            if not visited[i]:
                self.topo_util(i, visited, stack)
        stack.insert(0, node)
    
if __name__ == "__main__":
    g = Graph(7)
    g.add_edge(0, 1)
    g.add_edge(1, 2)
    g.add_edge(2, 4)
    g.add_edge(1, 4)
    g.add_edge(3, 1)
    g.add_edge(5, 6)
    # print g.graph
    # g.dfs()
    # g.topological(4)
