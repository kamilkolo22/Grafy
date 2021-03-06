from random import seed
from random import random
import numpy as np
from FunkcjeGrafy import *


def random_graph(n, p):
    rand_graph = {}
    for i in range(1, n + 1):
        add_vertex(rand_graph, i)
        for j in range(1, i):
            if random() < p:
                add_edge(rand_graph, [i, j])
    return rand_graph


def graph_to_matrix(graph):
    vertices = list(graph.keys())
    n = len(graph)
    matrix = np.zeros((n, n)).astype(int)
    for v in graph:
        for e in graph[v]:
            matrix[vertices.index(v)][vertices.index(e)] += 1
    return matrix, vertices


def matrix_to_graph(vertices, matrix):
    n = len(matrix)
    if len(vertices) < n:
        raise ValueError('lista wierzchołków jest za krótka!')
    graph = {x: [] for x in vertices}
    for i in range(n):
        for j in range(n):
            if matrix[i][j] > 0:
                graph[vertices[i]].append(vertices[j])
    return graph


if __name__ == '__main__':
    # Testy
    seed(2021)
    graph = random_graph(5, 0.5)
    print(graph)
    matrix = graph_to_matrix(graph)[0]
    print(graph_to_matrix(graph)[1])
    print_graph(graph)
    print(matrix)
    g = matrix_to_graph(['a', 'b', 'c', 'd', 'e'], matrix)
    print(g)
