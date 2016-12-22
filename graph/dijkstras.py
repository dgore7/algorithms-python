from collections import defaultdict

class Graph:
    def __init__(self):
        self.nodes = set()
        self.edges = defaultdict(list)
        self.distances = {}

    def add_node(self, value):
        self.nodes.add(value)

    def __contains__(self, item):
        return item in self.nodes

    def add_edge(self, from_node, to_node, distance):
        self.edges[from_node].append(to_node)
        self.edges[to_node].append(from_node)
        self.distances[(from_node, to_node)] = distance

def dijkstra(graph, source):
    visited = {source : 0}
    path = {}

    unsettled_nodes = set(graph.nodes)
    while unsettled_nodes:
        current = get_min_node(unsettled_nodes, visited)
        unsettled_nodes.remove(current)

        for edge in graph.edges[current]:

            tup = (current, edge) if (current, edge) in graph.distances else (edge, current)
            weight = graph.distances[tup] + visited[current]
            if edge not in visited or weight < visited[edge]:
                visited[edge] = weight
                path[edge] = current
    return visited, path




def get_min_node(nodes, visited):
    min_node = None
    min_distance = None
    for node in nodes:
        if node not in visited:
            continue
        if min_node == None:
            min_node = node
        elif visited[node] < visited[min_node]:
            min_node = node
    return min_node


for t in range(int(input())):
    graph = Graph()
    n, m = [int(i) for i in input().split()]
    for i in range(m):
        u, v, w = [int(j) for j in input().split()]
        if u not in graph:
            graph.add_node(u)
        if v not in graph:
            graph.add_node(v)
        graph.add_edge(u, v, w)
    source = int(input())
    dist, path = dijkstra(graph, source)
    for node, distance in dist.items():
        if node == source:
            continue
        print(distance, end=" ")