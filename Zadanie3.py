from Zajecia2 import *
from Zajecia3 import connected_components


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


def DFSsort(graph, v, S, colors):
    if colors[v] == 'grey':
        print('graf posiada cykl')
        return False
    if colors[v] == 'green':
        return True
    colors[v] = 'grey'
    for u in graph[v]:
        if not DFSsort(graph, u, S, colors):
            return False
    colors[v] = 'green'
    S.append(v)
    return True


def TopologicalSort(graph):
    colors = {key: 'white' for key in graph}
    S = []
    for v in graph:
        if not colors[v] == 'white':
            continue
        if not DFSsort(graph, v, S, colors):
            return S
    components = strongly_connected_components(graph, S.copy())[1:]
    if len(components) == len(graph):
        print('Kolejność jest porządkiem topologicznym')
    else:
        print('Brak porządku topologicznego')
    return S


def transpose_graph(graph):
    graph_t = {key: [] for key in graph}
    for v in graph:
        for u in graph[v]:
            graph_t[u].append(v)
    return graph_t


def strongly_connected_components(graph, order):
    order.reverse()
    graph_t = transpose_graph(graph)
    graph_ordered = {key: graph_t[key] for key in order}
    return connected_componentsBFS(graph_ordered)


def connected_componentsBFS(graph):
    def BFS(v):
        queue.append(v)
        while len(queue) > 0:
            v = queue.pop(0)
            VT[-1].add(v)
            for u in graph[v]:
                if u in VT[0]:
                    continue
                queue.append(u)
                VT[0].add(u)

    VT = [set([])]
    queue = []
    for v in graph:
        if v not in VT[0]:
            VT[0].add(v)
            VT.append({v})
            BFS(v)
    return VT

# # testy dla graph_from_edges
graph2 = graph_from_edges("Dane/lista.txt")
# graph_to_edges(graph2, 'graf.txt')
# print(graph2)
#
# testy dla TopologicalSort
tree = {}
add_arc(tree, (1, 2))
add_arc(tree, (4, 5))
add_arc(tree, (1, 3))
add_arc(tree, (3, 4))
add_arc(tree, (3, 5))
# print(tree)
print(TopologicalSort(tree))

comp = connected_components(graph2)
print(comp)
print(connected_componentsBFS(graph2))

