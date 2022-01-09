def print_matrix(vertices, matrix):
    """ Wypisuje na ekranie graf jako macierz sasiedstwa"""
    n = len(matrix)
    if (vertices is not None) and (len(vertices) == n):
        vv = vertices
    else:
        vv = range(1, n+1)
    for i in range(n):
        print(vv[i], ":", end="")
        for j in range(n):
            if matrix[i, j]:
                print(" ", vv[j], end="")
        print("")


def print_graph(graph):
    """Wypisuje graf jako slownik pythona"""
    for v in graph:
        print(v, ":", end="")
        for u in graph[v]:
            print(" ", u, end="")
        print("")


def add_vertex(graph, vertex):
    """Nowy wierzcholek do istniejacego grafu"""
    if vertex not in graph:
        graph[vertex] = []


def add_arc(graph, arc):
    """Dodaje nowy luk, graf prosty skierowany"""
    u, v = arc
    add_vertex(graph, u)
    add_vertex(graph, v)
    if v not in graph[u]:
        graph[u].append(v)


def add_edge(graph, edge):
    """Dodaje krawedz do grafu"""
    u, v = edge
    add_vertex(graph, u)
    add_vertex(graph, v)
    if u == v:
        raise ValueError("pętla!")
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)


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
