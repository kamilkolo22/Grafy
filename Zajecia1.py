import numpy as np
from FunkcjeGrafy import *


if __name__ == '__main__':
    vertices = ['a', 'b', 'c', 'd', 'e', 'f']
    matrix = np.array([[0, 1, 1, 0, 0, 0],
                      [1, 0, 1, 0, 0, 0],
                      [1, 1, 0, 1, 1, 0],
                      [0, 0, 1, 0, 1, 0],
                      [0, 0, 1, 1, 0, 0],
                      [0, 0, 0, 0, 0, 0]])
    graph = {
        'a': ['b', 'c'],
        'b': ['a', 'c'],
        'c': ['a', 'b', 'd', 'e'],
        'd': ['c', 'e'],
        'e': ['c', 'd'],
        'f': []
    }

    print(graph)
    print_matrix(vertices, matrix)
    print_graph(graph)

    add_vertex(graph, "g")
    add_arc(graph, ['a', 'g'])
    add_edge(graph, ['h', 'd'])
    print_graph(graph)

    """ Tworzenie grafów losowych """
    seed(2021)

    n = 10
    p = 1 / 3
    random_graph = {}
    for i in range(1, n + 1):
        add_vertex(random_graph, i)
        for j in range(1, i):
            if random() < p:
                add_edge(random_graph, [i, j])

    print_graph(random_graph)
