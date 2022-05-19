## https://leetcode.com/problems/number-of-ways-to-arrive-at-destination/
class Solution(object):
    def countPaths(self, n, roads):
        graph = collections.defaultdict(list)
        for u, v, w in roads:
            graph[u].append((v, w))
            graph[v].append((u, w))
        
        def dijkstra(src, dst):
            ways = [0]*n
            ways[src] = 1
            cost = [float('inf')]*n
            cost[src] = 0

            pq = [(0,src)]
            while pq:
                curr_cost, node = heapq.heappop(pq)
                if cost[node] < curr_cost:
                    continue
                for nei, wt in graph[node]:
                    if curr_cost + wt < cost[nei]:
                        cost[nei] = curr_cost + wt
                        ways[nei] = ways[node]
                        heapq.heappush(pq,(curr_cost + wt, nei))
                    elif curr_cost + wt == cost[nei]:
                        ways[nei] = (ways[nei] + ways[node])%(10**9 + 7)

            return ways[dst]
        
        return dijkstra(0, n-1)


## https://leetcode.com/problems/cheapest-flights-within-k-stops/
class Solution(object):
    def findCheapestPrice(self, n, flights, src, dst, k):
        # Solution - 1 (Bellman-Ford)
        prices = [float('inf')]*n
        prices[src] = 0
        
        while k >= 0:
            tmp = [x for x in prices]
            for s, d, p in flights:
                if prices[s] == float('inf'):
                    continue
                if p + prices[s] < tmp[d]:
                    tmp[d] = p + prices[s]
            prices = tmp
            
            k -= 1
            
        return -1 if prices[dst] == float('inf') else prices[dst]
        
        
        graph = collections.defaultdict(list)
        for s, d, p in flights:
            graph[s].append([d, p])
            
        # Solution - 2 (BFS)
#         prices = [float('inf')]*n
        
#         q = [(src, 0, k)]
        
#         while q:
#             node, price, k = q.pop(0)
            
#             if node == dst or k < 0:
#                 continue
            
#             for nei, p in graph[node]:
#                 if p + price >= prices[nei]:
#                     continue
#                 prices[nei] = p + price
#                 q.append([nei, price + p, k - 1])
                
#         return -1 if prices[dst] == float('inf') else prices[dst]
    
    
        # Solution - 3 (Dijkstra)
#         vis = [0]*n
        
#         pq = [[0, src, k+1]]
        
#         while pq:
#             cost, node, steps = heapq.heappop(pq)
            
#             if node == dst:
#                 return cost
            
#             if vis[node] >= steps:
#                 continue
                
#             vis[node] = steps
#             for nei, p in graph[node]:
#                 heapq.heappush(pq, [cost + p, nei, steps - 1])

#         return -1

        
        # Solution - 4 (DFS) TLE, dont submit
#         def dfs(k, curr_node, cost):
#             if curr_node == dst:
#                 self.res = min(self.res, cost)
            
#             if k < 0:
#                 return
#             visited[curr_node] = True
#             for nei, p in graph[curr_node]:
#                 if not visited[nei]:
#                     if cost + p >= self.res:
#                         continue
#                     dfs(k - 1, nei, cost + p)
#             visited[curr_node] = False
                
#         self.res = float('inf')
#         visited = [False]*n
#         dfs(k, src, 0)
#         return -1 if self.res == float('inf') else self.res




## https://leetcode.com/problems/number-of-provinces/
class Solution(object):
    def findCircleNum(self, isConnected):
#         def dfs(i):
#             visited[i] = True
#             for nei, adj in enumerate(isConnected[i]):
#                 if adj and not visited[nei]:
#                     dfs(nei)
        
#         n = len(isConnected)
#         count = 0
#         visited = [False]*n
#         for i in range(n):
#             if not visited[i]:
#                 dfs(i)
#                 count += 1
#         return count

        def find(x):
            if x == self.root[x]:
                return x
            self.root[x] = find(self.root[x])
            return self.root[x]
        
        def union(x, y):
            rootX = find(x)
            rootY = find(y)
            if rootX != rootY:
                if self.rank[rootX] > self.rank[rootY]:
                    self.root[rootY] = rootX
                elif self.rank[rootX] < self.rank[rootY]:
                    self.root[rootX] = rootY
                else:
                    self.root[rootY] = rootX
                    self.rank[rootX] += 1
                return 1
            return 0
        
        self.root = [i for i in range(len(isConnected))]
        self.rank = [1]*(len(isConnected))
        
        count = len(isConnected)
        for i in range(len(isConnected)):
            for j, adj in enumerate(isConnected[i]):
                if adj:
                    count -= union(i, j)
        return count        





# https://leetcode.com/problems/partition-to-k-equal-sum-subsets/
# TODO
class Solution(object):
    def canPartitionKSubsets(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        if sum(nums)%k:
            return False
        nums.sort(reverse=True)
        target = sum(nums)/k
        used = [False]*len(nums)
        
        def backtrack(index, k, curr_sum):
            if k == 0:
                return True
            if curr_sum == target:
                return backtrack(0, k-1, 0)
            for i in range(index, len(nums)):
                if used[i] or curr_sum + nums[i] > target:
                    continue
                used[i] = True
                if backtrack(i+1, k, curr_sum + nums[i]):
                    return True
                used[i] = False
            
            return False
        
        return backtrack(0, k, 0)





## LC 1692. Count Ways to Distribute Candies
## https://leetcode.ca/2020-07-18-1692-Count-Ways-to-Distribute-Candies/

# There are n unique candies (labeled 1 through n) and k bags.
# You are asked to distribute all the candies into the bags such that every bag has at least one candy.

# Given two integers, n and k, return the number of different ways to distribute the candies.
# As the answer may be too large, return it modulo 10^9 + 7.

# Input: n = 3, k = 2
# Output: 3
# Explanation: You can distribute 3 candies into 2 bags in 3 ways:
# (1), (2,3)
# (1,2), (3)
# (1,3), (2)

# Example 2:
# Input: n = 4, k = 2
# Output: 6
# Explanation: You can distribute 4 candies into 2 bags in 7 ways:
# (1), (2,3,4)
# (1,2), (3,4)
# (1,3), (2,4)
# (1,4), (2,3)
# (1,2,3), (4)
# (1,2,4), (3)
# (1,3,4), (2)

# Example 3:

# Input: n = 20, k = 5
# Output: 206085257
# Explanation: You can distribute 20 candies into 5 bags in 1881780996 ways. 1881780996 modulo 10^9 + 7 = 206085257.

def ways_to_distribute(n, k):
	mod  = 10**9 + 7
	dp = [[0]*n for _ in range(k)]
	for j in range(n):
		dp[0][j] = 1

	for i in range(1, k):
		for j in range(i, n):
			dp[i][j] = (dp[i-1][j-1] + dp[i][j-1]*(i+1)) % mod

	return dp[-1][-1]

# print ways_to_distribute(20, 5)



# https://www.geeksforgeeks.org/count-ways-to-distribute-m-items-among-n-people/?ref=lbp
# Given m and n representing number of mangoes and number of people respectively. Task is to calculate number of ways to distribute m mangoes among n people. Considering both variables m and n, we arrive at 4 typical use cases where mangoes and people are considered to be:
# 1) Both identical 
# 2) Unique and identical respectively 
# 3) Identical and unique respectively 
# 4) Both unique 
# Input :  m = 3, n = 2
# Output : 4
# There are four ways
# 3 + 0, 1 + 2, 2 + 1 and 0 + 3 

# Input :  m = 13, n = 6
# Output : 8568

# Input :  m = 11, n = 3
# Output : 78

def binomial_coefficient(n, r):
	res = 1
	if r > n - r:
		r = n - r

	for i in range(r):
		res *= (n-i)
		res /= (i+1)

	return res

def calculate_ways(m, n):
	if m < n:
		return 0

	ways = binomial_coefficient(m + n - 1, n-1)
	return ways

# print calculate_ways(3, 2)


## https://www.geeksforgeeks.org/count-number-ways-reach-given-score-game/
# Consider a game where a player can score 3 or 5 or 10 points in a move. 
# Given a total score n, find number of ways to reach the given score.

# Examples: 
# Input: n = 20
# Output: 4
# There are following 4 ways to reach 20
# (10, 10)
# (5, 5, 10)
# (5, 5, 5, 5)
# (3, 3, 3, 3, 3, 5)

# Input: n = 13
# Output: 2
# There are following 2 ways to reach 13
# (3, 5, 5)
# (3, 10)

def count(n):
 
    # table[i] will store count of solutions for value i.
    # Initialize all table values as 0.
    table = [0 for i in range(n+1)]
 
    # Base case (If given value is 0)
    table[0] = 1
 
    # One by one consider given 3 moves and update the
    # table[] values after the index greater than or equal
    # to the value of the picked move.
    for i in range(3, n+1):
        table[i] += table[i-3]
    for i in range(5, n+1):
        table[i] += table[i-5]
    for i in range(10, n+1):
        table[i] += table[i-10]
 
    return table[n]
 
# Driver Program
n = 20
# print('Count for', n, 'is', count(n))



# # Question 2: Robot Room Cleaner
# # There is a cleaning robot which is cleaning a rectangular grid of size Nx M, represented by array R consisting of N strings. Rows are numbered from 0 to N-1 (from top to bottom) and columns are numbered from 0 to M-1 (from left to right).

# # The robot starts cleaning in the top-left corner, facing rightwards. It moves in a straight line for as long as it can, i.e. while there is an unoccupied grid square ahead of it. When it cannot move forward, it rotates 90 degrees clockwise and tries to move forward again until it encounters another obstacle, and so on. Dots in the array (".") represent empty squares and 'x's represent occupied squares (ones the robot cannot move through). Each square that the robot occupied at least once is considered clean. The robot moves indefinitely.

# # Write a function:

# # int solution (vector &R);

# # that, given an array R consisting of N strings, each of length M, representing the grid, returns the number of clean squares.

# # Examples:

# # Given A = [...X..","..XX","..X..."], your function should return 6.

# #include<bits/stdc++.h>
# using namespace std;

# unordered_map<string, bool> visited;
# unordered_set<string> st;
# vector<string> grid;
    
# void dfs(int i, int j, int dir) {
#     int m = grid.size();
#     int n = grid[0].size();
#     if(i == m || i == -1 || j == n || j == -1) {
#         if(i == m) dfs(i-1, j, 2);
#         else if(i == -1) dfs(i+1, j, 0);
#         else if(j == n) dfs(i, j-1, 1);
#         else if(j == -1) dfs(i, j+1, 3);
#         return;
#     }
#     string key = to_string(i) + "_" + to_string(j) + "_" + to_string(dir);
#     if(visited.find(key) != visited.end()) return;
    
#     visited[key] = true;
#     if(grid[i][j] != 'X') {
#         string k = to_string(i) + "_" + to_string(j);
#         st.insert(k);
#         if(dir == 0) dfs(i, j+1, 0);
#         else if(dir == 1) dfs(i+1, j, 1);
#         else if(dir == 2) dfs(i, j-1, 2);
#         else if(dir == 3) dfs(i-1, j, 3);
#     }
#     else {
#         if(dir == 0) dfs(i, j-1, 1);
#         else if(dir == 1) dfs(i-1, j, 2);
#         else if(dir == 2) dfs(i, j+1, 3);
#         else if(dir == 3) dfs(i+1, j, 0);
#     }
#     return;
# }






# We have a graph (directed acyclic graph) that means if there is a path from a to b then there is no 
# path from b to a. Given a source and a target we have to find the longest path from source to target.

# // 3 (number of vertices)
# // 1 2
# // 2 3
# // 1 3
# // Source 1 and Target 3... Output ( 1 2 3) We have to output the longest path

# // 5 (number of vertices)
# // 1 2
# // 2 3
# // 3 4
# // 1 4
# // 4 5
# // Source 1 and Target 5... Output ( 1 2 3 4 5) We have to output the longest path.





