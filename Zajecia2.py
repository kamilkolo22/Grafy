import numpy as np
from random import random
from random import seed
from FunkcjeGrafy import *
from Zadanie1 import *
from copy import deepcopy


def graph_from_edges(filename, directed=False):
    """Wczytuję graf z pliku tesktowego, który w każdej lini zawiera opis jednej krawędzi"""
    graph = {}
    with open(filename, 'r') as f:
        for line in f:
            words = line.split()
            if len(words) == 1:
                add_vertex(graph, words[0])
            elif len(words) >= 2:
                if directed:
                    add_arc(graph, (words[0], words[1]))
                else:
                    add_edge(graph, (words[0], words[1]))
    return graph


def prufer(tree):
    """Kod Prufera drzewa - podany jako napis"""
    tr = deepcopy(tree)
    code = ""
    for i in range(len(tree)-2):
        for x in sorted(tr):
            if len(tr[x]) == 1:     #liść pierwszy - jednocześnie najmniejszy
                v = tr[x][0]
                code += f" {v}"
                tr[v].remove(x)     #usuwam x z listy sąsiadów
                tr.pop(x)   #usuwam x z drzewa
                break
    return code


def tree_from_prufer(code):
    """Tworzenie drzewa z kodu Prufera - cod jest napisem, drzewo grafem w formie listy sasiadów"""
    clist = [int(x) for x in code.split()]
    n = len(clist) + 2
    vert = [v for v in range(1, n+1)]
    tree = {}
    for v in vert:
        add_vertex(tree, v)
    for i in range(n-2):
        for x in vert:
            if x not in clist:  #x - najminiejszy liść
                v = clist.pop(0)
                add_edge(tree, (x, v))
                vert.remove(x)
                break
    add_edge(tree, (vert[0], vert[1]))
    return tree

def graph_to_neighbourslist(graph, filename):
    """
    Zapisuje graf jako listę sąsiedztwa w pliku tekstowym filename
    """
    file = open(filename, "w")
    for v in graph:
        neigh_list = "{}:".format(v)    #używamy format do budowy napisu - listy sąsiadów na razie postaci 'v:'
        for u in graph[v]:
            neigh_list = neigh_list + " {}".format(u) #dołączamy u na koniec napisu listy sąsiadów
        neigh_list = neigh_list + '\n'  #koniec wiersza
        file.write(neigh_list)          #zapisujemy wiersz do pliku
    file.close()

if __name__ == '__main__':
    # graph = graph_from_edges("Dane/ubranie.txt", directed=True)
    # print_graph(graph)

    graph2 = graph_from_edges("Dane/lista.txt")
    print_graph(graph2)
    tree = {}
    add_edge(tree, (1, 2))
    add_edge(tree, (1, 3))
    add_edge(tree, (3, 4))
    add_edge(tree, (3, 5))

    graph_to_neighbourslist(graph2, 'graph.txt')
    print_graph(tree)
    code = prufer(tree)
    print(code)
    print_graph(tree_from_prufer(code))
