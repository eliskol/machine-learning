class DecisionTree:

    def fit(self, datapoints):
        self.classes = self.find_classes(datapoints)
        self.tree = []
        self.dimensions = len(datapoints[0]) - 1
        while something:

        return

    def compute_gini_impurity(self, datapoints):
        num_of_datapoints = len(datapoints)
        classes = self.find_classes(datapoints)
        gini_impurity = 1
        for data_class in classes:
            proportion = 0
            for datapoint in datapoints:
                datapoint_class = datapoint[0]
                if datapoint_class == data_class:
                    proportion += 1
            proportion = proportion / num_of_datapoints
            gini_impurity -= proportion ** 2
        return gini_impurity

    def find_classes(self, datapoints):
        classes = []
        for datapoint in datapoints:
            datapoint_class = datapoint[0]
            if datapoint_class not in classes:
                classes.append(datapoint_class)
        return classes

    def find_best_split(self, datapoints):
        num_of_classes = len(self.find_classes(datapoints))
        impurity_before_split = self.compute_gini_impurity(datapoints)
        if num_of_classes == 1:
            return None
        for i in range(self.dimensions):
            possible_split_points = find_possible_split_points(self, i + 1, datapoints)
            for possible_split_point in possible_split_points:
                left_split_points = [datapoint for datapoint in datapoints if datapoint[i + 1] < possible_split_point]
                right_split_points [datapoint for datapoint in datapoints if datapoint[i + 1] > possible_split_point]

                

    def find_possible_split_points(self, split_axis, datapoints):
        sorted_datapoints = sorted(datapoints, split_axis)
        possible_split_points = []
        for i in range(len(sorted_datapoints)):
            possible_split_points.append((sorted_datapoints[i] + sorted_datapoints[i + 1]) / 2)
        return possible_split_points


class TreeNode:
    def __init__(self, split_index, split_coordinate, datapoints):
        self.split_index = split_index
        self.split_coordinate = split_coordinate
        self.datapoints = self.datapoints
