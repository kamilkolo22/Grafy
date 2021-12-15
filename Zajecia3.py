from FunkcjeGrafy import *
from Zajecia2 import *

# Przechodzenie drzewa
lista = []
def preorder(tree, v, pred=None):
    """Przechodze od wierzcholka v zakaldajca ze jeko poprzednikeiem jest wierzcholek pred"""
    if pred is None:
        lista.clear()
    lista.append(v)
    for u in tree[v]:
        if u != pred:
            preorder(tree, u, v)

def postorder(tree, v, pred=None):
    if pred is None:
        lista.clear()
    for u in tree[v]:
        if u != pred:
            preorder(tree, u, v)
    lista.append(v)

# tree = {}
# add_edge(tree, (1, 2))
# add_edge(tree, (1, 3))
# add_edge(tree, (3, 4))
# add_edge(tree, (3, 5))
# add_edge(tree, (2, 6))
# add_edge(tree, (2, 7))
#
# preorder(tree, 1)
# print(lista)

def connected_components(graph):
    """Znajduje spojne skladowe w grafie nieskierowanym. Jako wynik zwraca liste zbiorow wierzcholkow.
    Uwaga: pierwszym elementoem listy jest zbior wszystkiech wiercholkow grafu"""
    # VT lista zbiorow VT[i] zbiorow i-tej spojnej skaldowej
    def DFS(v):
        """Przeszukiwanie grafu w glab"""
        for u in graph[v]:
            if u not in VT[0]:  # u jeszce nie odwiedzony
                VT[0].add(u)   # u juz odwiedzony
                VT[-1].add(u)  # w ostatniej spojnej skladowej
                DFS(u)

    VT = [set([])]
    for v in graph:
        if v not in VT[0]:
            VT[0].add(v)
            VT.append({v})
            DFS(v)
    return VT

# graph = graph_from_edges('Dane/lista.txt')
# VT = connected_components(graph)
# print(VT)

def connected_components_graphs(graph):
    """Zwraca spojne skladowe grafow w formie listy grafow"""
    VT = connected_components(graph)
    components = []
    for vt in VT[1:]:
        components.append({k: v for k, v in graph.items() if k in vt})
    return components

def connected_components_graphs2(graph):
    VT = connected_components(graph)
    print("Liczba spojnych skladowych: ", len(VT) - 1)
    # Kazda spojna skladowa przepisujemy jako graf
    components = []
    for vt in VT[1:]:
        comp = {}
        for v in vt:
            comp[v] = graph[v]
        components.append(comp)
    return components

# graph = graph_from_edges('Dane/lista.txt')
# comp = connected_components_graphs(graph)
# print(len(comp))
# print(comp)

def distance(graph, v):
    """Znajduje i zwraca jako wynik wektor (slownik) odleglosci od wierzcholka v do wierzcholka
    w tej samej spojnej skladowej"""
    dist = {v: 0}  # zalazek slownika odleglosci
    kolejka = [v]
    while len(kolejka) > 0:
        u = kolejka.pop(0)
        for w in graph[u]:
            if w not in dist:
                dist[w] = dist[u] + 1
                kolejka.append(w)
    return dist

# graph = graph_from_edges('Dane/lista.txt')
# comp = connected_components_graphs2(graph)
# odl = distance(comp[0], 'D')
# print(odl)

if __name__ == '__main__':
    # Czy model G(n, p) jest dobrym opisem ekpsperymentu Millgrama z 1967 'small world phenomen'
    import sys
    sys.setrecursionlimit(2500)

    rgraph = random_graph(2000, 1/200)
    lista = connected_components_graphs2(rgraph)
    graph = lista[0]
    print(len(graph))

    md = {}
    ecc = {}
    for v in graph:
        dist = distance(graph, v)
        ecc[v] = max(dist.values())
        md[v] = sum(dist.values()) / len(dist)
    print(f"Promien: {min(ecc.values())}, Srednica: {max(ecc.values())}, srednio: {sum(md.values()) / len(md)}")
