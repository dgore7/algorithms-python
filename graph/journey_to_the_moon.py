import math

class Solution:
    def __init__(self):
        self.graph = {}
        N, I = [int(i) for i in input().split(" ")]
        for i in range(I):
            a, b = [int(i) for i in input().split(" ")]
            if a not in self.graph:
                self.graph[a] = []
            if b not in self.graph:
                self.graph[b] = []
            self.graph[a].append(b)
            self.graph[b].append(a)

        visited = set()
        result = 0
        for i in range(N):
            if i not in visited and i in self.graph:
                path = []
                self.dfs(i, path, visited)
                result += self.k_choose2(len(path))

        print(self.k_choose2(N) - result)

    def k_choose2(self, k):
        if k <= 1:
            return 1
        return math.factorial(k) // (2 * math.factorial(k-2))

    def dfs(self, current, path=list(), visited=set()):

        stack = [current]
        path.append(current)
        visited.add(current)
        while stack:
            current = stack.pop()
            for node in self.graph[current]:
                if node not in visited:
                    path.append(node)
                    visited.add(node)
                    stack.append(node)


Solution()
