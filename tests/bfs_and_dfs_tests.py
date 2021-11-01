import sys
sys.path.insert(1, "/home/coder/project/src")

from graph import *


graph_1 = Graph([[4, 0], [4, 8], [4, 6], [0, 8], [0, 2], [0, 3], [2, 3], [3, 2], [6, 3], [3, 1], [3, 9], [3, 5], [5, 7]])
print(graph_1.breadth_first(4))
print(graph_1.depth_first(4))
print(graph_1.depth_first(8))