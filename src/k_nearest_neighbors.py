from helper import find_min


class KNearestNeighborsClassifier:
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
            distances.append(distance_squared**0.5)
        return distances

    def classify(self, input_point):
        distances = self.compute_distances(input_point)
        classifications = []
        for i in range(self.k):
            smallest_distance = find_min(distances)
            index_of_smallest_distance = distances.index(smallest_distance)
            classifications.append(self.classifications[index_of_smallest_distance])
            distances.pop(index_of_smallest_distance)

        classification_count_dict = {
            classification: 0 for classification in classifications
        }
        classification_with_max_count = classifications[0]

        for classification in classifications:
            classification_count_dict[classification] += 1
            if (
                classification_count_dict[classification]
                > classification_count_dict[classification_with_max_count]
            ):
                classification_with_max_count = classification

        return classification_with_max_count
