import sys
sys.path.insert(1, sys.path[0].replace('tests', 'src'))

from graph import Graph

test_edges_1 = [(1, 2), (2, 3), (3, 4), (3, 5), (4, 2)]
graph_1 = Graph(test_edges_1)
# assert graph_1.check_for_cycle() is True

test_edges_2 = [(1, 2), (2, 3), (3, 4), (4, 5), (6, 7), (7, 3)]
graph_2 = Graph(test_edges_2)
print(graph_2.check_for_cycle())
# assert graph_2.check_for_cycle() is False