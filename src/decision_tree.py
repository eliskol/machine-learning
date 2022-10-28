class DecisionTree:

    def fit(self, datapoints):
        self.classes = self.find_classes(datapoints)
        self.dimensions = len(datapoints[0]) - 1
        self.datapoints = datapoints
        self.root_node = TreeNode(self.datapoints)
        self.split_queue = [self.root_node]
        while len(self.split_queue) > 0:
            current_node_to_split = self.split_queue[0]
            self.split_queue.pop(0)
            best_split_parameters = self.find_best_split(current_node_to_split.datapoints)
            if best_split_parameters is None:
                continue
            current_node_to_split.set_split_parameters(best_split_parameters[0], best_split_parameters[1])
            current_node_to_split.set_child_nodes(best_split_parameters[2])
            self.split_queue.append(current_node_to_split.left_child)
            self.split_queue.append(current_node_to_split.right_child)

    def predict(self, datapoint):
        current_node = self.root_node
        while current_node.left_child is not None:
            split_axis = current_node.split_axis
            split_point = current_node.split_point
            if datapoint[split_axis - 1] <= split_point:
                current_node = current_node.left_child
            else:
                current_node = current_node.right_child
        return current_node.majority_class

    @staticmethod
    def compute_gini_impurity(datapoints):
        num_of_datapoints = len(datapoints)
        classes = DecisionTree.find_classes(datapoints)
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

    @staticmethod
    def find_classes(datapoints):
        classes = []
        for datapoint in datapoints:
            datapoint_class = datapoint[0]
            if datapoint_class not in classes:
                classes.append(datapoint_class)
        return classes

    def find_best_split(self, datapoints):
        num_of_classes = len(self.find_classes(datapoints))
        num_of_datapoints = len(datapoints)
        initial_impurity = DecisionTree().compute_gini_impurity(datapoints)
        # print(initial_impurity)
        if num_of_classes == 1:
            return None
        highest_decrease_in_impurity = 0
        for i in range(self.dimensions):
            possible_split_points = self.find_possible_split_points(i + 1, datapoints)
            for possible_split_point in possible_split_points:
                left_split_points = [datapoint for datapoint in datapoints if datapoint[i + 1] < possible_split_point]
                right_split_points = [datapoint for datapoint in datapoints if datapoint[i + 1] > possible_split_point]

                left_node = TreeNode(left_split_points)
                right_node = TreeNode(right_split_points)

                weighted_impurity_of_left_node = (left_node.num_of_datapoints / num_of_datapoints) * left_node.gini_impurity
                weighted_impurity_of_right_node = (right_node.num_of_datapoints / num_of_datapoints) * right_node.gini_impurity

                decrease_in_impurity = initial_impurity - (weighted_impurity_of_left_node + weighted_impurity_of_right_node)

                if decrease_in_impurity > highest_decrease_in_impurity:
                    best_split_axis = i + 1
                    best_split_point = possible_split_point
                    nodes_after_split = [left_node, right_node]
                    highest_decrease_in_impurity = decrease_in_impurity
        if highest_decrease_in_impurity == 0:
            return None
        return [best_split_axis, best_split_point, nodes_after_split]

    def find_possible_split_points(self, split_axis, datapoints):
        sorted_datapoints = sorted(datapoints, key=lambda x: x[split_axis])
        possible_split_points = []
        for i in range(len(sorted_datapoints) - 1):
            current_datapoint_value_on_split_axis = sorted_datapoints[i][split_axis]
            next_datapoint_value_on_split_axis = sorted_datapoints[i + 1][split_axis]
            if current_datapoint_value_on_split_axis != next_datapoint_value_on_split_axis:
                # fix these two lines; add intermediate variable
                possible_split_points.append((current_datapoint_value_on_split_axis + next_datapoint_value_on_split_axis) / 2)
        return possible_split_points


class TreeNode:
    def __init__(self, datapoints):
        self.datapoints = datapoints
        self.gini_impurity = DecisionTree().compute_gini_impurity(datapoints)
        self.num_of_datapoints = len(datapoints)
        self.left_child, self.right_child = None, None
        self.majority_class = self.find_majority_class()

    def set_split_parameters(self, split_axis, split_point):
        self.split_axis = split_axis
        self.split_point = split_point

    def set_child_nodes(self, child_nodes):
        self.left_child = child_nodes[0]
        self.right_child = child_nodes[1]

    def find_majority_class(self):
        class_dict = {}
        for datapoint in self.datapoints:
            class_of_datapoint = datapoint[0]
            if class_of_datapoint in class_dict:
                class_dict[class_of_datapoint] += 1
            else:
                class_dict[class_of_datapoint] = 1
        return max(class_dict)


data = [['Shortbread', 0.15, 0.2],
        ['Shortbread', 0.15, 0.3],
        ['Shortbread', 0.2, 0.25],
        ['Shortbread', 0.25, 0.4],
        ['Shortbread', 0.3, 0.35],
        ['Sugar', 0.05, 0.25],
        ['Sugar', 0.05, 0.35],
        ['Sugar', 0.1, 0.3],
        ['Sugar', 0.15, 0.4],
        ['Sugar', 0.25, 0.35]]

bruh = DecisionTree()
bruh.fit(data)
print(bruh.predict([0.27, 0.35]))