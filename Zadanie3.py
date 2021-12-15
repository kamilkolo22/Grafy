from Zajecia2 import *


def graph_to_edges(graph, filename):
    edges_list = ''
    used = []
    for v in graph:
        if not graph[v]:
            edges_list += f'{v}\n'
        for u in graph[v]:
            if u not in used:
                edges_list += f'{v} {u}\n'
        used.append(v)
    f = open(filename, 'w')
    f.write(edges_list)
    f.close()


def TopologicalSort(graph, v, S, visited=None, processed=None):
    if visited is None:
        visited = []
        processed = []
    if v in visited:
        return False
    if v in processed:
        return True
    visited.append(v)
    for u in graph[v]:
        if not TopologicalSort(graph, u, S, visited, processed):
            return False
    processed.append(v)
    S.append(v)
    print(S)
    return True


graph2 = graph_from_edges("Dane/lista.txt")
print(graph2)
graph_to_edges(graph2, 'graf.txt')

S = []
TopologicalSort(graph2, 'A', S)
print(S)
