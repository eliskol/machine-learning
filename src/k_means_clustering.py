from hashlib import new


class KMeans:
    def __init__(self, initial_clusters, data):
        self.initial_clusters = initial_clusters
        self.data = data

    def find_centers(self):
        length_of_datapoints = len(self.data[0])
        centers = {cluster_index: [0 for i in range(len(self.data[0]))] for cluster_index in self.clusters}
        for index, cluster in self.clusters.items():
            num_of_points_in_cluster = len(cluster)
            for point_index in cluster:
                for coord_index in range(length_of_datapoints):
                    centers[index][coord_index] += self.data[point_index][coord_index] / num_of_points_in_cluster

        self.centers = centers

    def find_distance_from_center(self, point_index, cluster_index):
        cluster_center = self.centers[cluster_index]
        point = self.data[point_index]
        length_of_point = len(point)
        distance = 0
        for i in range(length_of_point):
            distance += (point[i] - cluster_center[i]) ** 2
        distance **= 0.5  # sqrt
        return distance

    def reassign_clusters(self):
        new_clusters = {cluster_index: [] for cluster_index in self.clusters}
        for point_index in range(len(self.data)):
            distances = {cluster_index: self.find_distance_from_center(point_index, cluster_index) for cluster_index in self.clusters}
            closest_cluster = min(distances, key=distances.get)
            new_clusters[closest_cluster].append(point_index)
        self.clusters = new_clusters

    def run(self):
        previous_clusters = {}
        removed_clusters = []
        self.clusters = self.initial_clusters
        while previous_clusters != self.clusters:
            previous_clusters = self.clusters
            for cluster_index in list(self.clusters.keys()):
                if len(self.clusters[cluster_index]) == 0:
                    self.clusters.pop(cluster_index)
                    removed_clusters.append(cluster_index)

            self.find_centers()
            self.reassign_clusters()
        for cluster_index in removed_clusters:
            self.clusters[cluster_index] = []
