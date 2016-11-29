#! /bin/usr/python3


class GraphNode:
    def __init__(self, string):
        self.string = string
        self.length = len(string)
        self.is_file = '.' in string
        self.adj = []

    def __repr__(self):
        return '<GraphNode {}>'.format(self.string)


class Solution:
    def longest_dir_path(self, path):
        cur_str = ''
        last_root = {}
        level = 0
        path += "\n"
        for n in path:
            if n == '\t':
                level += 1
                continue
            if n =='\n':
                x = GraphNode(cur_str)
                if level > 0:
                    last_root[level-1].adj.append(x)
                else:
                    root = x
                last_root[level] = x
                level = 0
                cur_str = ''
                continue
            cur_str += n
        return self.dfs(last_root[0])

    def dfs(self, root):
        stack = [root]
        visited = set()
        distance = {root: 0}
        pre = {root: None}
        max_distance = 0
        max_node = None

        while stack:
            node = stack.pop()
            if node not in visited:
                for neighbor in node.adj:
                    if neighbor not in distance:
                        distance[neighbor] = 0

                    # update distance with the maximum distance so far
                    if distance[neighbor] < distance[node] + node.length:
                        distance[neighbor] = distance[node] + node.length
                        pre[neighbor] = node


                        if distance[neighbor] > max_distance and neighbor.is_file:
                            max_distance = distance[neighbor]
                            max_node = neighbor
                    stack.append(neighbor)

        if not max_node:
            return -1

        length = 0
        v = max_node
        while v != None:
            length += v.length + 1
            v = pre[v]
        length -= 1
        return length
