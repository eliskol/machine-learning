class KMeans:
    def __init__(self, initial_clusters, data):
        self.initial_clusters = initial_clusters
        self.data = data
        self.clusters = initial_clusters

    def find_center_of_cluster(self, cluster):
        average_data_point = [0 for col in self.data[0]]
        for index in cluster:
            current_data_point = self.data[index]
            for col_index in range(len(self.data[0])):
                current_col_value = current_data_point[col_index]
                average_data_point[col_index] += current_col_value
        average_data_point = [col / len(cluster) for col in average_data_point]
        return average_data_point

    def find_index_of_closest_cluster(self, point_index, cluster_centers):
        distance_dict = {cluster_index: 0 for cluster_index in self.initial_clusters}
        for cluster_center_index in cluster_centers:
            distance = 0
            for coord_index in range(len(cluster_centers[cluster_center_index])):
                distance += (self.data[point_index][coord_index] - cluster_centers[cluster_center_index][coord_index]) ** 2
            distance_dict[cluster_center_index] = distance

        min_distance = min(distance_dict.values())
        for key in distance_dict:
            if distance_dict[key] == min_distance:
                return key

    def run(self):
        old_clusters = self.initial_clusters
        while old_clusters != self.clusters or old_clusters == self.initial_clusters:
            old_clusters = self.clusters
            self.clusters = {cluster_index: [] for cluster_index in self.clusters}
            cluster_centers = {index: self.find_center_of_cluster(
                old_clusters[index]) for index in old_clusters}
            for cluster_index in old_clusters:
                cluster = old_clusters[cluster_index]
                for point_index in cluster:
                    index_of_closest_cluster = self.find_index_of_closest_cluster(point_index, cluster_centers)
                    self.clusters[index_of_closest_cluster].append(point_index)

        return self.clusters


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

initial_clusters = {
    1: [0, 3, 6, 9, 12, 15, 18],
    2: [1, 4, 7, 10, 13, 16],
    3: [2, 5, 8, 11, 14, 17]
}

bruh = KMeans(initial_clusters, data)
print(bruh.run())
