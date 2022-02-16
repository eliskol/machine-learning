class KMeans:
    def __init__(self, initial_clusters, data):
        self.initial_clusters = initial_clusters
        self.data = data
        self.clusters = initial_clusters

    def find_center_of_cluster(self, cluster_index):
        average_data_point = [0 for col in self.data[0]]
        if len(self.old_clusters[cluster_index]) == 0: return None
        for index in self.old_clusters[cluster_index]:
            current_data_point = self.data[index]
            for col_index in range(len(self.data[0])):
                current_col_value = current_data_point[col_index]
                average_data_point[col_index] += current_col_value
        average_data_point = [col / len(self.clusters[cluster_index]) for col in average_data_point]
        return average_data_point

    def find_squared_distance_from_center(self, point_index, cluster_index):
        center_of_cluster = self.find_center_of_cluster(cluster_index)
        squared_distance = 0
        for coord_index in range(len(self.data[point_index])):
            squared_distance += (self.data[point_index][coord_index] -
                         center_of_cluster[coord_index]) ** 2
        return squared_distance

    def find_index_of_closest_cluster(self, point_index, cluster_centers):
        distance_dict = {cluster_index: 0 for cluster_index in self.initial_clusters}
        for cluster_center_index in cluster_centers:
            # print(cluster_center_index)
            if cluster_centers[cluster_center_index] == None: continue
            else:
                distance = 0
                for coord_index in range(len(cluster_centers[cluster_center_index])):
                    distance += (self.data[point_index][coord_index] - cluster_centers[cluster_center_index][coord_index]) ** 2
                distance_dict[cluster_center_index] = distance ** 0.5  # distance was squared, so take the sqrt

        min_distance = min(distance_dict.values())
        for key in distance_dict:
            if distance_dict[key] == min_distance:
                return key

    def run(self):
        self.old_clusters = self.initial_clusters
        while self.old_clusters != self.clusters or (self.old_clusters == self.initial_clusters and len(self.initial_clusters) != 1):
            self.clusters = {cluster_index: [] for cluster_index in self.clusters}
            self.old_clusters = self.clusters
            cluster_centers = {cluster_index: self.find_center_of_cluster(cluster_index) for cluster_index in self.old_clusters}
            for cluster_index in self.old_clusters:
                cluster = self.old_clusters[cluster_index]
                for point_index in cluster:
                    index_of_closest_cluster = self.find_index_of_closest_cluster(point_index, cluster_centers)
                    self.clusters[index_of_closest_cluster].append(point_index)

        # return self.clusters
