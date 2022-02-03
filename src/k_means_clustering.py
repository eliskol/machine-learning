class KMeans:
    def __init__(self, initial_clusters, data):
        self.initial_clusters = initial_clusters
        self.data = data

    def __average_of_cluster(self, cluster):
        average_data_point = [0 for col in self.data[0]]
        for index in cluster:
            current_data_point = self.data[index]
            for col_index in range(len(self.data[0])):
                current_col_value = current_data_point[col_index]
                average_data_point[col_index] += current_col_value
        average_data_point = [col / len(cluster) for col in average_data_point]
        return average_data_point

    def __distance_from

    def run(self):
        while