parent = {}
rank = {}


def make_set(v):
    parent[v] = v
    rank[v] = 0


def find(v):
    if v != parent[v]:
        parent[v] = find(parent[v])
    return parent[v]


def union(v, w):
    v = find(v)
    w = find(w)
    if v != w:
        if rank[v] < rank[w]:
            parent[v] = w
        else:
            parent[w] = v
            if rank[w] == rank[v]:
                rank[w] += 1


def kruskal():
    n, m = [int(i) for i in input().split(" ")]
    for i in range(1, n + 1):
        make_set(i)
    edges = []
    for i in range(m):
        u, v, w = [int(i) for i in input().split(" ")]
        edges.append((w, u, v))
    edges.sort()
    min_spanning_tree = 0
    for edge in edges:
        if find(edge[1]) != find(edge[2]):
            union(edge[1], edge[2])
            min_spanning_tree += edge[0]
    return min_spanning_tree


print(kruskal())
