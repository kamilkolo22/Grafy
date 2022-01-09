from FunkcjeGrafy import *
import numpy as np


graph = graph_from_edges("Dane/graf_belman_ford.txt")
print(graph)

def belman_ford(wgraph, s):
    # Init
    dist = {}
    pred = {}
    for v in wgraph:
        dist[v] = np.inf
        pred[v] = None
    dist[s] = 0
    for i in range(len(wgraph)-1):
        test = True
        for v in wgraph:
            for (u, w) in wgraph[v]:
                if dist[u] <= dist[v] + int(w):
                    continue
                test = False
                dist[u] = dist[v] + int(w)
                pred[u] = v
        if test:
            return dist, pred
    # Sprawdzenie czy istnieje cykl ujemny
    for v in wgraph:
        for (u, w) in wgraph[v]:
            if dist[u] > dist[v] + int(w):
                print('Uwaga, graf ma ujemny cykl')
                return dist, pred
    return dist, pred


def floyd_warshal(wgraph):
    # Init
    n = len(wgraph)
    vertixes = list(wgraph.keys())
    matrix = np.zeros((n, n))
    for i in range(n):
        for j in range(n):
            if not i == j:
                matrix[i, j] = np.inf
                for (u, w) in wgraph[vertixes[i]]:
                    matrix[i, vertixes.index(u)] = w
    for k in range(n):
        for i in range(n):
            for j in range(n):
                if matrix[i, j] > matrix[i, k] + matrix[k, j]:
                    matrix[i, j] = matrix[i, k] + matrix[k, j]
    # Sprawdzenie czy istnieje cykl ujemny
    for v in wgraph:
        for (u, w) in wgraph[v]:
            i = vertixes.index(v)
            j = vertixes.index(u)
            if matrix[i, j] > matrix[i, j] + int(w):
                print('Uwaga, graf ma ujemny cykl')
                return matrix
    return matrix


print(belman_ford(graph, 'A'))
print(floyd_warshal(graph))
