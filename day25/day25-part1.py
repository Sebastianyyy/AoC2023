from collections import defaultdict
import networkx as nx

if __name__ == '__main__':
    with open(file='input.txt') as f:
        lines = f.readlines()
    Graph = nx.Graph()
    for line in lines:
        node, neighbors = line.strip().split(':')
        neighbors = neighbors.split()
        Graph.add_node(node)
        Graph.add_edges_from((node, neighbor) for neighbor in neighbors)
    to_del=nx.minimum_edge_cut(Graph)
    Graph.remove_edges_from(to_del)
    groups=list(nx.connected_components(Graph))
    print(len(groups[0])*len(groups[1]))