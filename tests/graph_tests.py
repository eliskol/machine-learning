import sys
sys.path[0] = '/workspace/machine-learning/src'

from graph import Graph

graph_1 = Graph([[0, 1], [1, 2], [2, 3], [2, 4], [4, 0], [5, 0]])
graph_2 = Graph([(0, 1), (1, 0), (2, 3), (3, 0), (1, 4), (0, 4), (4, 5), (4, 6), (5, 6)])

assert graph_1.get_children(2) == [3, 4]
assert graph_1.get_parents(0) == [4, 5]

assert graph_2.get_parents(0) == [1, 3]
assert graph_2.get_children(4) == [5, 6]
#ignore this