from collections import defaultdict
from itertools import combinations
import networkx as nx


class subset:
    def __init__(self, p, r):
        self.parent = p
        self.rank = r


def DFS(s, vertices, disconnected):
    stack = []
    visited = {i: False for i in vertices}
    stack.append(s)
    count_vertices = 0
    top_edge = defaultdict(int)
    while stack:
        s = stack[-1]
        stack.pop()
        if (not visited[s]):
            visited[s] = True
            count_vertices += 1
        for node in vertices[s]:
            if not visited[node] and (node, s) not in disconnected and (s, node) not in disconnected:
                stack.append(node)
                top_edge[tuple(sorted((node, s)))] += 1
    return top_edge


if __name__ == '__main__':
    with open(file='input.txt') as f:
        lines = f.readlines()
    Graph = nx.Graph()
    for line in lines:
        node, neighbors = line.strip().split(':')
        neighbors = neighbors.split()
        Graph.add_node(node)
        Graph.add_edges_from((node, neighbor) for neighbor in neighbors)
    to_del = nx.minimum_edge_cut(Graph)
    Graph.remove_edges_from(to_del)
    groups = list(nx.connected_components(Graph))
    print(len(groups[0])*len(groups[1]))
