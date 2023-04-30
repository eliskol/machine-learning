import sys

sys.path.insert(1, sys.path[0].replace("tests", "src"))

from weighted_graph import WeightedGraph

weights = {
    (0, 1): 3,
    (1, 0): 3,
    (1, 7): 4,
    (7, 1): 4,
    (7, 2): 2,
    (2, 7): 2,
    (2, 5): 1,
    (5, 2): 1,
    (5, 6): 8,
    (6, 5): 8,
    (0, 3): 2,
    (3, 0): 2,
    (3, 2): 6,
    (2, 3): 6,
    (3, 4): 1,
    (4, 3): 1,
    (4, 8): 8,
    (8, 4): 8,
    (8, 0): 4,
    (0, 8): 4,
}

weighted_graph = WeightedGraph(weights)
assert [weighted_graph.calc_distance(8, n) for n in range(9)] == [
    4,
    7,
    12,
    6,
    7,
    13,
    21,
    11,
    0,
]

assert weighted_graph.calc_shortest_path(8, 4) == [8, 0, 3, 4]
assert weighted_graph.calc_shortest_path(8, 7) == [8, 0, 1, 7]
assert weighted_graph.calc_shortest_path(8, 6) == [8, 0, 3, 2, 5, 6]
