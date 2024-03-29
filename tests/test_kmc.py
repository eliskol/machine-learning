import sys

sys.path.insert(1, sys.path[0].replace("tests", "src"))
from k_means_clustering import KMeans


data = [
    [0.14, 0.14, 0.28, 0.44],
    [0.22, 0.1, 0.45, 0.33],
    [0.1, 0.19, 0.25, 0.4],
    [0.02, 0.08, 0.43, 0.45],
    [0.16, 0.08, 0.35, 0.3],
    [0.14, 0.17, 0.31, 0.38],
    [0.05, 0.14, 0.35, 0.5],
    [0.1, 0.21, 0.28, 0.44],
    [0.04, 0.08, 0.35, 0.47],
    [0.11, 0.13, 0.28, 0.45],
    [0.0, 0.07, 0.34, 0.65],
    [0.2, 0.05, 0.4, 0.37],
    [0.12, 0.15, 0.33, 0.45],
    [0.25, 0.1, 0.3, 0.35],
    [0.0, 0.1, 0.4, 0.5],
    [0.15, 0.2, 0.3, 0.37],
    [0.0, 0.13, 0.4, 0.49],
    [0.22, 0.07, 0.4, 0.38],
    [0.2, 0.18, 0.3, 0.4],
]

initial_clusters = {
    1: [0, 3, 6, 9, 12, 15, 18],
    2: [1, 4, 7, 10, 13, 16],
    3: [2, 5, 8, 11, 14, 17],
}

kmeans = KMeans(initial_clusters, data)
kmeans.run()
assert kmeans.clusters == {
    1: [0, 9, 12, 15, 18, 7, 2, 5],
    2: [6, 10, 16, 14, 3, 8],
    3: [1, 4, 13, 11, 17],
}
