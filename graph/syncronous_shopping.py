class GraphNode:

    def __init__(self, id, offerings=list()):
        self.adj = []
        self.offerings = offerings



class Solution:

    def __init__(self):
        N, M, K = [int(i) for i in input().split(" ")]
        self.graph = {}
        for i in range(1,N+1):
            offerings = [int(j) for j in input().split(" ")]
            offerings.pop(0)
            node = GraphNode(i, offerings)
            self.graph[i] = node
        for i in range(M):
            x, y, z = [int(j) for j in input().split(' ')]
            self.graph[x].adj.append((y, z))
            self.graph[y].adj.append((x, z))