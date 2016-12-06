class Node:
    def __init__(self, id, next):
        self.id = id
        self.size = 0
        self.next = next


class Graph:
    def __init__(self, cap):
        self.cap = cap
        self.adj = [None for i in range(cap+1)]

    def add_edge(self, v, w):
        v_node = Node(v, self.adj[w])
        self.adj[w] = v_node
        w_node = Node(w, self.adj[v])
        self.adj[v] = w_node


class Solution:
    def __init__(self):
        n, m = [int(i) for i in input().split(" ")]
        self.graph = Graph(n)
        for iter in range(m):
            verts = [int(i) for i in input().split(" ")]
            self.graph.add_edge(*verts)
        print(self.dfs(1))

    def dfs(self, source) -> int:
        visited = [False for i in range(self.graph.cap+1)]
        count = [0] # used as a pointer to an int
        self.__dfs(source, visited, count)
        return count[0]

    def __dfs(self, source, visited, count) -> int:
        visited[source] = True
        size = 1
        w = self.graph.adj[source]
        while w != None:
            if not visited[w.id]:
                component_size =  self.__dfs(w.id, visited, count)
                if component_size % 2 == 0:
                    # make a cut
                    count[0] += 1
                else:
                    size += component_size
            w = w.next
        return size

Solution()