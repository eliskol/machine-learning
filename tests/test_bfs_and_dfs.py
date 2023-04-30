import sys

sys.path.insert(1, "/home/coder/project/src")

from graph import *


graph_1 = Graph(
    [
        [4, 0],
        [4, 8],
        [4, 6],
        [0, 8],
        [0, 2],
        [0, 3],
        [2, 3],
        [3, 2],
        [6, 3],
        [3, 1],
        [3, 9],
        [3, 5],
        [5, 7],
    ]
)
graph_2 = Graph(
    [[0, 1], [0, 2], [0, 3], [1, 2], [2, 3], [3, 4], [3, 5], [3, 6], [6, 7], [6, 8]]
)

assert graph_1.breadth_first(4) == [4, 0, 8, 6, 2, 3, 1, 9, 5, 7]
assert graph_1.depth_first(4) == [4, 6, 3, 5, 7, 9, 1, 2, 8, 0]
assert graph_2.breadth_first(0) == [0, 1, 2, 3, 4, 5, 6, 7, 8]
assert graph_2.depth_first(0) == [0, 3, 6, 8, 7, 5, 4, 2, 1]
