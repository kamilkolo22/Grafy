from numpy import random


def new_node(value):
    '''Nowy wierzcholek drzewa'''
    return {'val': value, 'n': 1, 'left': None, 'right': None}


def add_value(tree, value):
    '''Dodanie nowej wartosci do drzewa'''
    if value < tree['val']:
        if tree['left'] is None:
            tree['left'] = new_node(value)
        else:
            add_value(tree['left'], value)
    elif value > tree['val']:
        if tree['right'] is None:
            tree['right'] = new_node(value)
        else:
            add_value(tree['right'], value)
    else:
        tree['n'] += 1


def print_inorder(tree):
    if tree['left'] is not None:
        print_inorder(tree['left'])
    print(f"{tree['val']}: {tree['n']}")
    if tree['right'] is not None:
        print_inorder(tree['right'])


tree = new_node(random.randint(1, 100))
for i in range(1000):
    add_value(tree, random.randint(1, 100))

print_inorder(tree)
