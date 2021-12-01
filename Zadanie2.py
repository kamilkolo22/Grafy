from FunkcjeGrafy import *
from copy import deepcopy
from random import random


def graph_from_neighbourlist(filename, directed=False):
    with open(filename, 'r') as f:
        graph = {}
        for line in f:
            vert = line[0]
            add_vertex(graph, vert)
            for v in line[2:].split():
                add_vertex(graph, v)
                if directed:
                    add_arc(graph, (vert, v))
                else:
                    add_edge(graph, (vert, v))
    return graph


def preorder(tree):
    visited = [list(tree.keys())[0]]
    check_neighbors(tree, visited, visited[0])
    return visited


def check_neighbors(tree, visited, v):
    for neighbor in tree[v]:
        if neighbor not in visited:
            visited.append(neighbor)
            check_neighbors(tree, visited, neighbor)
    if len(visited) >= len(tree):
        return
    else:
        index = visited.index(v)
        check_neighbors(tree, visited, visited[index-1])


def postorder(tree):
    tr = deepcopy(tree)
    root = list(tr.keys())[0]
    visited = []
    for n in range(len(tree) - 1):
        for v in tr:
            if len(tr[v]) <= 1 and v != root:
                visited.append(v)
                find_parent(tr, v)
                tr.pop(v)
                break
    visited.append(root)
    return visited


def find_parent(tree, child):
    for v in tree:
        if child in tree[v]:
            tree[v].remove(child)
            return


def random_bipartite_graph(n, p):
    random_graph = {}
    for i in range(1, 2*n+1):
        add_vertex(random_graph, i)
    for a in range(1, n+1):
        for b in range(n+1, 2*n+1):
            if random() < p:
                add_edge(random_graph, [a, b])
    return random_graph

print(graph_from_neighbourlist('graph.txt'))

tree = {}
add_edge(tree, (1, 2))
add_edge(tree, (1, 3))
add_edge(tree, (3, 4))
add_edge(tree, (3, 5))
add_edge(tree, (2, 6))
add_edge(tree, (2, 7))

print(tree)
print(preorder(tree))
print(tree)
print(postorder(tree))
print(random_bipartite_graph(4, 0.5))
