from k_means_clustering import KMeans

data = [[0.14, 0.14, 0.28, 0.44],
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
        [0.2, 0.18, 0.3, 0.4]]

for num_k in range(1, 10):
    initial_clusters = {i + 1: [] for i in range(num_k)}
    for row_index in range(0, len(data)):
        initial_clusters[(row_index % num_k) + 1].append(row_index)
    # print(initial_clusters)
    bruh = KMeans(initial_clusters, data)
    bruh.run()
    squared_error = 0
    for cluster_index in bruh.clusters:
        # print(cluster_index)
        if len(bruh.clusters[cluster_index]) == 0: print('')
        else:
            for row_index in bruh.clusters[cluster_index]:
                squared_error += bruh.find_squared_distance_from_center(row_index, cluster_index)
    print(bruh.clusters)
    print(num_k, squared_error)