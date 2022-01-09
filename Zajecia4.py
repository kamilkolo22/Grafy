from FunkcjeGrafy import *
from queue import PriorityQueue  # gotowe kolejki prirtetowe


def graph_from_edges(filename, directed=False):
    """Wczytuję graf z pliku tesktowego, który w każdej lini zawiera opis jednej krawędzi oraz waga danej krawedzi"""
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            if len(words) == 1:
                add_vertex(graph, words[0])
            elif len(words) == 2:
                if directed:
                    add_arc(graph, (words[0], words[1]))
                else:
                    add_edge(graph, (words[0], words[1]))
            elif len(words) >= 3:
                if directed:
                    add_arc(graph, (words[0], words[1]))
                    graph[words[0]][-1] = (words[1], words[2])
                else:
                    add_edge(graph, (words[0], words[1]))
                    graph[words[0]][-1] = (words[1], words[2])
                    graph[words[1]][-1] = (words[0], words[2])
    return graph

# graph = graph_from_edges("Dane/graf_w.txt")
# print(graph)

# Minimalne drzewa spinajace
def MinSpanningTree(wgraph):
    """Algorytm Jarnika-Prima - minimalne drzewa spinajace
    Dla nieksierowanych grafow wazonych zwraca pare (waga, drzewo), gdzie waga to waga drzewa a
    drzewo to minimalne drzewo spinajcace"""
    for v in wgraph:  # wybieramy jeden wierzcholek
        break
    tree = {v: []}
    weight = 0
    q = PriorityQueue()
    for (u, w) in wgraph[v]:
        q.put((int(w), v, u))
    while not q.empty():
        (w, v, u) = q.get()
        if u not in tree:
            weight += w
            tree[u] = [(v, w)]
            tree[v].append((u, w))
            for (x, w) in wgraph[u]:
                if x not in tree:
                    q.put((int(w), u, x))
    if len(tree) < len(wgraph):
        print('Graf niespojny - zwrocone dzrewo dla jendej spojnej skladeowej.')
    return weight, tree


graph1 = graph_from_edges("Dane/graf_w.txt")
# (wagi, tree) = MinSpanningTree(graph1)
# print(wagi)
# print(tree)

# Najkrotsze sciezki
def Dijkstra(wgraph, s):
    """Najkrotsze sciezki miedzy z wierzcholka s"""
    # Init
    dist = {}
    pred = {}
    for v in wgraph:
        dist[v] = 2**31
        pred[v] = None
    dist[s] = 0
    q = PriorityQueue()
    q.put((0, s))
    V = set()  # zbiór wierzchołkow przetworzonych
    while not q.empty():
        (d, u) = q.get()
        if u not in V:
            V.add(u)
            for (v, w) in wgraph[u]:   # relax
                if dist[v] > dist[u] + int(w):
                    dist[v] = dist[u] + int(w)
                    pred[v] = u
                    q.put((dist[v], v))
    return dist, pred

(dist, pred) = Dijkstra(graph1, "A")
print(dist)
print(pred)

# graph2 = graph_from_edges("Dane/wagi0.txt")
# (dist, pred) = Dijkstra(graph2, "A")
# print(dist)
# print(pred)
#
# graph3 = graph_from_edges("Dane/wagi1.txt")
# (dist, pred) = Dijkstra(graph3, "1")
