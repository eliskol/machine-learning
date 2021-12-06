from helper import find_min


class KNearestNeighborsClassifier(k):

    def __init__(self, k):
        self.k = k

    def fit(self, x, y):
        self.points = x
        self.classifications = y

    def compute_distances(self, input_point):
        distances = []
        for point in self.points:
            distance_squared = 0
            for i, dim in enumerate(input_point):
                distance_squared += (input_point[i] - point[i]) ** 2
            distances.append(distance_squared ** 0.5)
        return distances

    def classify(self, input_point):
        distances = self.compute_distances(input_point)
        classifications = []
        for i in range(k):
            smallest_distance = find_min(distances)
            index_of_smallest_distance = distances.index(smallest_distance)
            classifications.append(self.classifications[index_of_smallest_distance])
            distances.pop(index_of_smallest_distance)
        return 